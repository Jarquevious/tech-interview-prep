# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would
# have exactly one solution, and you may not
# use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Restate the problem
# So, my input is an array of integers and target k? And the function
# find two pairs of numbers that add up to the target? For example,
# input: y = [5,2,9] , k = 14; output: [5,14]. Is this an example of what 
# we are looking for? And y = [5,2,9], k = 12 would not be correct? and return none?

# Ask clarifying questions
# 1. Does this list contains arbitrary numbrs?
# 2. Does this list have both pos and neg numbers?
# 3. Are we optimizing for memory or speed? 
# 4. Is this sorted or unsorted?

# State your assumptions
# I assume we can use built in functions to solve it

# Think out loud
# Brainstorm solutions
# Im thinking loop through the list twice(for i,j), add the two elements and compare to k.
# if matches k, return(i and j) the two elements as a ordered pair. 

# Explain your rationale
# I use two for loops so I can access and different elements. Its a slow method because 
# of the two for loops. 

# Discuss tradeoffs
# We are trading speed for memory. In this example we are not adding elements
# to another data structure so we do not add any memery. 

# Suggest improvements
# We could use a hash table to optimise for speed. 


# Create an array with arbitrary numbers
arr = [2, 15, 11, 7, 100, 1000, 234, 76, 4, 2, 9]
# Target created
target = 6
# Created a function called two sum to find two sum, give it two parmeter the array and the target
def two_sum(arr, target):
# Inserted a for loop that searches the entire length of the array to find the first number that equals the target
    for i in range(len(arr)-1):
# Inserted a another for loop to find the second number that equals the target
        for j in range(i+1, len(arr)):
# Created a math formula to verify numbers equal the target
            if arr[i] +arr[j] == target:
# Print both arr[i] and arr[j] as an ordered par
                print(arr[i], arr[j])
# Inserted a 'return True' statement if the values equal target
                return True
# Inserted a 'return False' statement if values does not equal target
    return False
# Call the function with parameters for it to run
print(two_sum(arr, target))


#Credits:
#I received help from youtube: https://www.youtube.com/watch?v=gCin6Qz-eJQ
#I received help from Francis Tsang, Make School Student