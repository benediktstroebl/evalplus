from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Initialize a dictionary to store the current and previous distances
    current_distance = {key: float('inf') for key in numbers}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the difference between the two numbers
            current_distance[numbers[i]] = numbers[i] - numbers[j]
            
            # Check if the current distance is less than the threshold
            if current_distance[numbers[i]] < threshold:
                return True
                
    # If all distances are greater than the threshold, return False
    return False
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 8, 0.0]
threshold = 0.1