def twoNumberSum(array, targetSum):
    # Write your code here.
    seen = {}
    for num in array:
        if targetSum - num in seen: