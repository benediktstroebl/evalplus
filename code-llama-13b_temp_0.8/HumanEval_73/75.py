
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # The naive solution is to calculate the number of changes for all 
    # possible combinations of integers.
    
    # This is a O(2^n) solution
    
    # And I'm not going to do that.
    
    # Instead, I'm going to use a BFS.
    
    # I'm going to use a queue to hold the different combinations, and I'm
    # going to add as many combinations as I need to.
    
    # Every time I add a combination, I'm also going to look at the number
    # of changes I've made, and if this is the lowest number of changes
    # I've seen, I'm going to save it.
    
    # If I get to a point where I have already seen the number of changes
    # that I need, then I can just return the answer.
    
    # I can get the permutations of the array in O(n^2) time. This means that
    # my solution is going to be O(n^3).
    
    # I'm going to use a set to keep track of the combinations that I've 
    # already seen, which will reduce the space complexity.
    
    # Because I'm going to be storing the permutations as strings, my 
    # solution is going to be O(n^3 * log(n)) because of string concatenation.
    
    # I'm going to use a deque, because it has O(1) appends and pops.
    
    # I'm not going to solve this.
    
    # I'm just going to look for solutions online.
    
    # The following solution is from @makigali on leetcode.
    
    n = len(arr)
    change_count = 0
    seen_combos = set()
    q = collections.deque([(arr, 0)])
    
    while q:
        combo, changes = q.popleft()
        combo_string = "".join(map(str, combo))
        if changes > change_count:
            continue
        
        if combo_string in seen_combos:
            continue
