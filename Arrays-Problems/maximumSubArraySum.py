# Question: 1_____
# Find the Maximum Subarray Sum
# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# brute force approach
def maxSubArraySum(arr):
    maxSum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            maxSum = max(maxSum, sum)
    return maxSum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArraySum(arr))



# kadane's algorithm
def maxSubArraySumKadane(arr):
    maxSum = arr[0]
    currentSum = arr[0]
    for i in range(1, len(arr)):
        currentSum = max(arr[i], currentSum + arr[i])
        maxSum = max(maxSum, currentSum)
    return maxSum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArraySumKadane(arr))
