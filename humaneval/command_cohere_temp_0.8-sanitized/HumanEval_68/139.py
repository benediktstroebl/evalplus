from typing import List
from itertools import accumulate
def pluck(nums: List[int]) -> List[int]:
    # Filter even numbers and accumulate (sum and index)
    evens = list(filter(lambda x: x % 2 == 0, nums))
    accums = list(accumulate(evens, fillvalue=0))
    
    # Return the smallest even number and its index
    smallest_even, index = next((k, i) for i, (n, _) in enumerate(zip(accums, evens)) if n == min(accums))
    
    return [smallest_even, index] if smallest_even != 0 else []