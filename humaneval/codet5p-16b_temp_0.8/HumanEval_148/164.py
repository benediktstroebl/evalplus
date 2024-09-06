
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

    orbits = {'Mercury': 0.2408467, 'Venus': 0.61519726, 'Earth': 1, 'Mars': 1.881, 'Jupiter': 11.86, 'Saturn': 29.447, 'Uranus': 84.016846, 'Neptune': 164.79132}
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    planets_tuple = tuple(planets)

    if planet1 not in planets or planet2 not in planets:
        return ()

    if planet1 == planet2:
        return planets_tuple

    planet1_orbits = orbits[planet1]
    planet2_orbits = orbits[planet2]
    proximity = abs(planet1_orbits - planet2_orbits)
    return planets_tuple[proximity - 1]
