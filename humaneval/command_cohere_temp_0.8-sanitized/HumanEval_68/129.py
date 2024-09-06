def pluck(arr):
    # Splitting the list into two lists with odd and even numbers
    odd, even = partition(arr, lambda x: x % 2 == 0)
    
    # If odd list is not empty, return the smallest value and its index
    if odd:
        return [odd[0], odd.index(odd[0])]
    
    # If even list is empty, return empty list
    if not even:
        return []
    
    # Sorting the even list and returning the smallest value and its index
    return [even[0], even.index(even[0])]
def partition(arr, predicate):
    pivot = arr.index(predicate(arr[0]))    # Split at the first element that matches the predicate
    left = [x for x in arr[:pivot]]         # Exclude the pivot element from the left list
    right = [x for x in arr[pivot+1:]]     # Exclude the pivot element from the right list
    return left, right