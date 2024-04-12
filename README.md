# Trapping-Rainwater-Problem
This repository contains a Python solution to the "Trapping Rain Water" problem using a prefix maximum approach.

Problem Description
Given an array of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: heights = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Solution Explanation
The solution uses the following approach:

Prefix Maximum Calculation:

Define a helper function get_prefix_max(h) to compute a prefix maximum array for a given list h.
This function calculates the maximum height encountered from the start up to each index in the input list h.
Compute Left and Right Prefix Maximums:

Calculate left as the prefix maximum of the input height array.
Calculate right as the prefix maximum of the reversed height array (and then reverse it back).
Calculate Trapped Water:

Iterate through each index i of the height array.
For each index, compute the trapped water above the current bar using:

water += max(min(left[i], right[i + 1]) - height[i], 0)
Here:
left[i] represents the maximum height encountered from the start up to index i.
right[i + 1] represents the maximum height encountered from the end up to index i.
min(left[i], right[i + 1]) - height[i] computes the water level at index i.
max(..., 0) ensures that negative values (where no water is trapped) are ignored.
Return Result:

The accumulated water value after iterating through all indices represents the total trapped water.
