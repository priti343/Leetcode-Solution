def max_subarray_sum(arr):
    current_sum = arr[0]  # running sum, starts as first element
    best_sum = arr[0]      # best sum found so far

    for i in range(1, len(arr)):
        # Decision: extend previous subarray, or start fresh here?
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update best_sum if current_sum is a new record
        best_sum = max(best_sum, current_sum)

    return best_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray_sum(arr))