
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
    # check if planet1 and planet2 are valid planet names
    if not isinstance(planet1,str) or not isinstance(planet2,str):
        return []
    # list of planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    # get the position of each planet
    positions = [getpos(p) for p in planets]
    # check if the position of the first planet is before or after the second
    # planet and sort the planets accordingly
    if positions[0] > positions[1]:
        planets.reverse()
    # find the position of the second planet
    positions.remove(positions[1])
    # find the position of the first planet
    positions.remove(positions[0])
    # check if the position of the first planet is before or after the second
    # planet and sort the planets accordingly
    if positions[0] > positions[1]:
        planets.reverse()
    # sort the planets by their proximity to the sun
    sorted_planets = sorted(planets, key=lambda p: p.getpos()[1])
    return tuple(sorted_planets[positions.index(positions[1])+1:])
