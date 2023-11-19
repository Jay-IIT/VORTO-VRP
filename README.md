# Vehicle Routing Problem 

## Problem Definition:

The VRP involves a set of loads, each with a defined pickup and dropoff location in a two-dimensional plane represented by Cartesian coordinates.
The objective is to assign these loads to drivers efficiently, minimizing the total cost, which is a function of both the number of drivers employed and the total driving time.

## Load Completion:

A load is completed by a driver by traveling from their current location to the load's pickup location, then to its dropoff location.
The time taken to travel between two points is calculated using the Euclidean distance formula.  

Each driver starts and ends their shift at a central depot located at 
(0,0) (0,0).A driver’s total drive time in a shift cannot exceed 720 minutes (12 hours).
Solution and Cost:

## A solution to the VRP consists of an assignment of all loads to drivers.
The total cost of a solution is calculated as:

$$500 \times \text{number of drivers} + \text{total number of driven minutes}$$

## Command to Run the Code

```
python solution.py TrainingProblems/problem1.txt  
```

## Evaluation

``` 
python evaluateShared.py --cmd "python solution.py" --problemDir TrainingProblems
```
## Example  Run
![!\[Alt text\](Evaluation.gif)
](docs/Evaluation.gif)

## Evaluated Output
```
mean cost: 27463.812844001357
mean run time: 77.8702974319458ms

```
