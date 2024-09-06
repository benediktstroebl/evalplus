
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    month_and_num = ["jan", "mar", "may", "jul", "aug", "sep", "oct", "dec"]
    month_and_num_2 = ["apr", "jun", "sep", "nov"]
    month_num = ["01", "03", "05", "07", "08", "10", "12"]

    day_num = []
    for days in day_list:
        day_num.append(str(days))

    given_date = re.split(r"-", date)

    if len(given_date) != 3:
        return False

    if given_date[0] not in month_num:
        return False

    if given_date[1] not in day_num:
        return False

    if given_date[2] not in year_list:
        return False

    return True

"""

What is the purpose of this?

Here's an example:

The input data	is	a	list	of	strings,	each	string	is	a	day	of	a	month.

For	the	first	month,	the	list	of	days	is	: ['31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
For	the	second	month,	the	list	of	days	is	: ['31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
For	the	third	month,	the	list	of	days	is	: ['31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

The output	should	be	the	number	of	days	that	the	last	day	in	a	month	presents	at	the	last	position	in	the	list.

The list	should	only	contain	digits.	The	list	is	sorted,	so	the	last	day	of	a	month	will	appear	on	the	last	position	in