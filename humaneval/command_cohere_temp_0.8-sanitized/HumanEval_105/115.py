def by_length(arr):
    # Sort the array and ignore strange numbers
    sorted_arr = sorted(arr if not num.is_strange() else [num for num in arr if not num.is_strange()])
    
    # Reverse the sorted array and translate digits to names
    translated_arr = ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'][::-1]*len(sorted_arr)
    
    return translated_arr if translated_arr else []
arr = [2, 1, 1, 4, 5, 8, 2, 3]