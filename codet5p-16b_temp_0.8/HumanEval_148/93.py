
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

    orbital_period = {
        'Mercury': 87.969,
        'Venus': 224.769,
        'Earth': 365.256,
        'Mars': 686.96,
        'Jupiter': 4332.59,
        'Saturn': 10759.37,
        'Uranus': 27805.45,
        'Neptune': 56846.52,
    }

    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

    return tuple(sorted((x for x in planets if orbital_period[x] > orbital_period[planet1] < orbital_period[planet2]), key=orbital_period.get))

