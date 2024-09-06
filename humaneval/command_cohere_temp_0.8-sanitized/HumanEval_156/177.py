import itertools
def int_to_mini_roman(num):
    if num < 1000:
        result = []
        for i in range(0, num + 1):
            temp = str(i)
            rom_num = ROMA[temp][0]
            if len(rom_num) > 1:
                result.append(rom_num[1:])
            else:
                result.append(rom_num)

        return ''.join(result)

    else:
        return "Error! Input exceeds restrictions."