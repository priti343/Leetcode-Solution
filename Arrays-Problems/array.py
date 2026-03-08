# =====================================================
# 📁 Arrays - LeetCode Solutions
# ===========================================================


# ------------------------------------------------------
# Problem 1: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# ------------------------------------------------------
class Solution:
    def twoSum(self, nums,target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(Solution().twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(Solution().twoSum([3, 3], 6))          # Output: [0, 1]   
print(Solution().twoSum([1, 2, 3], 7))       # Output: [] (no solution)