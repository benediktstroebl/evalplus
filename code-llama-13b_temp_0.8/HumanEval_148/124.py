
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
    solarsystem = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    solarpositions = [0.387, 0.723, 1.0, 1.524, 5.203, 9.537, 19.19, 30.06]
    # planet1 and planet2 are wrong if not in the solar system
    if planet1 not in solarsystem:
        return ()
    if planet2 not in solarsystem:
        return ()
    # planet1 and planet2 are wrong if they have the same position
    if solarpositions[solarsystem.index(planet1)] == solarpositions[solarsystem.index(planet2)]:
        return ()
    # determine positions
    p1 = solarsystem.index(planet1)
    p2 = solarsystem.index(planet2)
    # determine if the planets are next to each other
    if p1 == p2 + 1 or p2 == p1 + 1:
        return (solarsystem[p1 - 1], solarsystem[p2 + 1])
    # if not, return the planet in between
    if p1 > p2:
        return (solarsystem[p2 + 1], solarsystem[p1 - 1])
    else:
        return (solarsystem[p1 + 1], solarsystem[p2 - 1])

