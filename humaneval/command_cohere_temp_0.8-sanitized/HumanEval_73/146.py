def smallest_change(arr):
    # Count the number of odd elements in the array
    odd = sum(1 for elt in arr if elt % 2 != 0)
    
    # Count the number of duplicate elements, as these can be switched freely
    duplicates = sum(elt != arr.count(elt) for elt in set(arr))
    
    return max(odd, duplicates)