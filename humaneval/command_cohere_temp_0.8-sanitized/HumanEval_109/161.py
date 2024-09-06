def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize variables and sort the array
    prev = arr[0]
    moved = 0
    temp = arr[:]
    temp.sort()

    # Iterate through the sorted array
    for curr in temp:
        if curr <= prev:
            moved += 1
        else:
            # If the gap between the elements is more than 1, return False
            if moved > 1:
                return False
            
            # Reset the moved counter and compare the elements again
            moved = 1
            if curr != prev:
                return False
        
        prev = curr
    
    # If the last element is reached and the moved counter is 1, return True
    return moved == 1