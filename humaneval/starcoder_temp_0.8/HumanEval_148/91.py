
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
    solar_system = {'Mercury': 0.39, 'Venus': 0.72, 'Earth': 1,
                    'Mars': 1.52, 'Jupiter': 5.2, 'Saturn': 9.5,
                    'Uranus': 19.2, 'Neptune': 30}
    if planet1 in solar_system and planet2 in solar_system:
        return tuple(sorted([x for x in solar_system if (solar_system[x] > solar_system[planet1] and solar_system[x] < solar_system[planet2])]))
    else:
        return tuple([])
