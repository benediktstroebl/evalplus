

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    d = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A',
         11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K',
         21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U',
         31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
    y, x = abs(x), abs(x)
    if x == 0:
        return '0'
    array = []
    while x:
        x, m = divmod(x, base)
        array.append(d[m])
    array.append(d[x])
    array.reverse()
    return ''.join(array)
