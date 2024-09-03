def prod_signs(arr):
    if not_elements(arr):  # Check if the array is empty
        return None
    result = 1  # Initialize result with 1 (any non-zero number will have a positive product)
    
    for num in arr:
        result = result * (-num)  # Multiply each element by the negation of itself
    
    return result
def not_elements(arr):
    return len(arr) == 0
arr = [1, 2,2,-4]
result = prod_signs(arr)