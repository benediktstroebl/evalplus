Here's the solution:

def string_sequence(n: int) -> str:
    return f"0 {n}"*n 

This function uses the Python string formatting feature with the {n} argument to create a string that contains n copies of the character '0' separated by spaces, starting from index 0.