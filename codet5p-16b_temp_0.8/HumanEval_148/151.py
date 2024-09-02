
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

    planets = {
    "Mercury" : 0.387,
    "Venus" : 0.723,
    "Earth" : 1,
    "Mars" : 1.523,
    "Jupiter" : 5.203,
    "Saturn" : 9.537,
    "Uranus" : 19.213,
    "Neptune" : 30.061,
    }

    planets1 = planets.get(planet1, "Not a planet")
    planets2 = planets.get(planet2, "Not a planet")
    if planets1 == "Not a planet" or planets2 == "Not a planet":
        return ()
    difference = abs(planets1 - planets2)
    min_distance = planets1
    max_distance = planets2
    if planets1 > planets2:
        max_distance = planets1
        min_distance = planets2
    for planet in planets:
        distance = planets.get(planet)
        if distance > max_distance and distance < min_distance:
            min_distance = distance
            if min_distance
