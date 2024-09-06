def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, hundreds, tens, remainder = divmod(n, 1000)
        if thousands > 0: 
            return ""
        elif thousands == 0 and hundreds == 0: 
            if remainder == 0:
                return "i"
            elif remainder == 5:
                return "v"
            else:
                return str(remainder)
        elif thousands == 0 and hundreds == 0 and remainder == 0:
            return ""
        elif hundreds == 0: 
            if remainder == 0:
                return "x"
            elif remainder == 5:
                return "xv"
            else:
                return str(remainder) + "x"
        else:
            hundreds_str = self.int_to_mini_roman(hundreds)
            if remainder == 0:
                return hundreds_str
            elif remainder == 5:
                return hundreds_str + "v"
            else:
                return hundreds_str + str(remainder)