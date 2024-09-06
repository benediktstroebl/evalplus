
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
    # check if the input planets are correct
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] or planet2 not in [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]:
        return ()

    # create a list of all planets and their distances from the sun
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    distances = []
    for planet in planets:
        if planet == planet1:
            distances.append(1)
        else:
            distances.append(1000)
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            distances.append(
                distances[i] + distances[j] / 149597870700
                # convert astronomical units to kilometers
)

    # sort the planets by their proximity to the sun
    planets = sorted(planets, key=lambda x: distances[0] - distances[x])

    # create a list of all planets between the orbit of planet1 and planet2
    # and their proximity to the sun
    result = []
    for i in range(1, len(planets)):
        if distances[i] >= distances[planet1] and distances[i] <= distances[planet2]:
            result.append(planets[i])

    return result
