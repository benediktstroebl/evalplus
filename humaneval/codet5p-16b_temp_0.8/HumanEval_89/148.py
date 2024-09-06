
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    nums = list('abcdefghijklmnopqrstuvwxyz')
    nums2 = nums[-2::-2] + nums[-1::-2]
    nums3 = [i for i in nums if i not in nums2]
    nums4 = nums2 + nums3
    table = str.maketrans(nums, nums4)
    return s.translate(table)
