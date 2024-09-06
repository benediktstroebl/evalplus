def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    if odd % 2 == 0:
        return int(odd/2)
    else:
        return int((odd+1)/2)