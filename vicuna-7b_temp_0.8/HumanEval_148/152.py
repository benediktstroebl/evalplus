
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
    # Codes for verifying the validity of planet names
    if not any(c.isalpha() for c in planet1) or not any(c.isalpha() for c in planet2):
        return []
    elif planet1 == "Mercury" or planet2 == "Mercury":
        return []
    elif any(c.lower() == 's' for c in planet1) and any(c.lower() == 's' for c in planet2):
        return [(planet1, planet2) for planet1 in planets
                   for planet2 in planets if (planet1 < planet2)
                   and (planet1 > 'Mars')
                   and (planet2 > 'Mars')]
    else:
        return [(planet1, planet2) for planet1 in planets
                   for planet2 in planets if (planet1 < planet2)
                   and (planet1 > 'Jupiter')
                   and (planet2 < 'Jupiter')
                   and (planet2 > 'Saturn')]
