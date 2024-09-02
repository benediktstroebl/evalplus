
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

    planets = {'Mercury': 0.387, 'Venus': 0.723, 'Earth': 1, 'Mars': 1.524, 'Jupiter': 11.86, 'Saturn': 29.46, 'Uranus': 84.01, 'Neptune': 164.79}
    distance = planets[planet1] + planets[planet2]
    pl = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    pl1, pl2 = 0, 0
    for i in pl:
        if planets[i] < distance:
            pl2 = pl2 + 1
        else:
            break
    return tuple(pl[pl1: pl2])
