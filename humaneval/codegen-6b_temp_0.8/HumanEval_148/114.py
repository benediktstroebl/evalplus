
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    
    from math import modf
    from pprint import pprint
    from itertools import combinations
    def round_half_up(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier + 0.5) / multiplier
    
    #planet = {
    #    'Mercury':[0.35,0.47],
    #    'Venus':[0.72,0.75],
    #    'Earth':[1.0,1.0],
    #    'Mars':[1.52,1.52],
    #    'Jupiter':[5.2,5.15],
    #    'Saturn':[9.4,9.38],
    #    'Uranus':[19.2,19.12],
    #    'Neptune':[30.0,30.00]
    #}

    #planet = {
    #    'Mercury':[0.35,0.47],
    #    'Venus':[0.72,0.75],
    #    'Earth':[1.0,1.0],
    #    'Mars':[1.52,1.52],
    #    'Jupiter':[5.2,5.15],
    #    'Saturn':[9.4,9.38],
    #    'Uranus':[19.2,19.12],
    #    'Neptune':[30.0,30.00]
    #}

    planet = {
    'Mercury':[0.35,0.47],
    'Venus':[0.72,0.75],
    'Earth':[1.0,1.0],
    'Mars':[1.52,1.52],
    'Jupiter':[5.2,5.15],
    'Saturn':[9.4,9.38],
    'Uranus':[19.2,19.12],
    'Neptune':[30.0,30.00]
    }

    a = planet[planet1]
    b = planet[planet2]
    round_up =