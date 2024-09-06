
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
    # write your code here
    planets = ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    places = set()
    
    for planet in planets:
        if planet == planet1:
            continue
        if planet == planet2:
            return tuple()
        # equation of the orbit
        equation = (ra(planet, planet1) + \
                    dec(planet, planet1) - \
                    ra(planet, planet2) - \
                    dec(planet, planet2))/(r5(planet) - r5(planet2))
        if equation > 1 or equation < -1:
            equation = -1 - equation
        places.add(equation)
    return tuple(sorted(places))
