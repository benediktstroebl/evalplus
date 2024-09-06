
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

    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    orbital_r = {
    'Mercury': 58.98,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.5,
    'Saturn': 1429.4,
    'Uranus': 2871.6,
    'Neptune': 4495.1
    }
    
    if planet1 in planets and planet2 in planets:
        planet1_orb = orbital_r[planet1]
        planet2_orb = orbital_r[planet2]
        if planet1_orb < planet2_orb:
            return tuple(filter(lambda x: orbital_r[x] < planet2_orb and orbital_r[x] > planet1_orb, planets))
        else:
            return tuple(filter(lambda x: orbital_r[x] > planet2_orb and orbital_r[x] < planet
