# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

# Restate Question
# I am given an array nums, and a value represented by val? And I am writing a function to remove
# instances of the value in the array? Correct? And I should return a new length?
# For example, in example 1: given nums, my input should be nums = [3,2,2,3], val = 3; output = [2,2],
# length: 2. correct?

# Ask Clarifying Questions
# Are these numbers both positive and negative?
# How big is the list?
# Sorted or Unsorted? 

# Assumptions/Solutions
# I could compare every value and delete repeated values. 

# Improvements:
# We could use a binary search to find and delete 
# Or we could use a hashset to quickly find them and delete them. 


class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)





nums = [3,2,2,3]
val = 3
# nums = [0,1,2,2,3,0,4,2], val = 2
removeElement(self, nums, val)

