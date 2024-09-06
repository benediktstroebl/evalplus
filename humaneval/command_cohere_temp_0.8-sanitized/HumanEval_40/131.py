def triples_sum_to_zero(lst):
    # Define possible triple combinations and initialize boolean array
    n = len(lst)
    arr = [[j for j in range(n) if i != j and lst[i] + lst[j] != lst[k]] for i in range(n) for k in range(i+1, n)]
    # Initialize flag to False for if there is a triple that sums to zero
    flag = False
    # Loop through each combination of triple and check if sum is zero
    for t in range(len(arr)):
        if sum(arr[t]) == 0:
            flag = True
            break
    return flag