import math
import sys

def calculate_euclidean_distance(point_a, point_b):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

class Job:
    """Class representing a job with start and end points."""

    def __init__(self, job_id, start_point, end_point):
        self.id = job_id
        self.start = start_point
        self.end = end_point
        self.is_finished = False  # False - unfinished, True - finished
        self.travel_distance = calculate_euclidean_distance(start_point, end_point)

    def __repr__(self):
        return f'Job({self.id}, {self.start}, {self.end})'

class Driver:
    """Class representing a driver with assigned jobs."""

    def __init__(self, driver_id):
        self.jobs = []
        self.current_location = (0, 0)
        self.total_distance_travelled = 0
        self.id = driver_id

    def assign_job(self, job):
        """Assign a job to the driver and update distance."""
        self.jobs.append(job)
        self.total_distance_travelled += calculate_euclidean_distance(self.current_location, job.start) + job.travel_distance
        self.current_location = job.end

    def __repr__(self):
        return f'Driver({self.jobs})'
def read_and_process_data(file_path):
    """Read job data from a file and process it into jobs."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    jobs = {}
    for line in lines[1:]:  # Assuming the first line is a header
        load_number, pickup, dropoff = line.split()
        load_number = int(load_number)

        # Parsing the pickup and dropoff coordinates
        pickup = tuple(float(coord) for coord in pickup.strip('()').split(','))
        dropoff = tuple(float(coord) for coord in dropoff.strip('()').split(','))

        # Creating a Job object and storing it with the load number as key
        jobs[load_number] = Job(load_number, pickup, dropoff)

    return jobs

def assign_jobs_to_drivers(jobs):
    """Assign jobs to drivers."""
    jobs_remaining = list(jobs.keys())
    drivers = []
    driver_id = 1

    while jobs_remaining:
        driver = Driver(driver_id)
        initial_job_id = sorted(jobs_remaining, key=lambda x: calculate_euclidean_distance(jobs[x].start, driver.current_location))[0]
        driver.assign_job(jobs[initial_job_id])
        jobs_remaining.remove(initial_job_id)

        while driver.total_distance_travelled < 720:  # 12 hours * 60 minutes
            next_jobs = sorted([job_id for job_id in jobs_remaining if driver.total_distance_travelled + calculate_euclidean_distance(jobs[job_id].start, driver.current_location) + jobs[job_id].travel_distance + calculate_euclidean_distance(jobs[job_id].end, (0,0)) < 720], key=lambda x: calculate_euclidean_distance(jobs[x].start, driver.current_location))

            if not next_jobs:
                break

            next_job_id = next_jobs[0]
            driver.assign_job(jobs[next_job_id])
            jobs_remaining.remove(next_job_id)

        drivers.append(driver)
        driver_id += 1

    return drivers

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the input file path as an argument.")
        sys.exit(1)  
    input_file = sys.argv[1]
    jobs = read_and_process_data(input_file)
    drivers = assign_jobs_to_drivers(jobs)
    for driver in drivers:
        print([job.id for job in driver.jobs])
            