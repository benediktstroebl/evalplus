from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Initialize a flag to track if any valid pair is found
    found = False
    
    # Iterate over all pairs of numbers in the list
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
             # Calculate the distance between the current pair of numbers
             distance = abs(numbers[i] - numbers[j])
             
             # If the distance is less than the given threshold, set the flag to True
             if distance < threshold:
                 found = True
                 
                 # Return True immediately if a valid pair is found
                 if found: 
                     return True

    # Return the flag value if no valid pair is found
    return found