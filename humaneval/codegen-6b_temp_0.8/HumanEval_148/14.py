
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
    if planet1.lower() == "moon" or planet2.lower() == "moon":
        return ()
    if planet1.lower() == "sun":
        return (planet2,)
    if planet2.lower() == "sun":
        return (planet1,)
    between = []
    for planet in planets:
        if planet1 == planet:
            break
        between.append((planet, angleR(planet, planet1)))
        between.sort(key=lambda x: x[1])
    for planet in between:
        if planet[0] == planet2:
            return tuple([x[0] for x in between if x[1] <= angleR(planet2, planet1) <= x[1] + 2 * pi])
    return ()
