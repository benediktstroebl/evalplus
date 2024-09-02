
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
    if planet1 == "Mercury":
        return (planet1, "Venus")
    if planet1 == "Venus":
        return (planet1, "Earth", "Mars")
    if planet1 == "Earth":
        return (planet1, "Mars", "Jupiter")
    if planet1 == "Mars":
        return (planet1, "Jupiter", "Saturn")
    if planet1 == "Jupiter":
        return (planet1, "Saturn", "Uranus")
    if planet1 == "Saturn":
        return (planet1, "Uranus", "Neptune")
    if planet1 == "Uranus":
        return (planet1, "Neptune")
    if planet2 == "Earth":
        return ()
    if planet2 == "Mercury":
        return ()
    if planet2 == "Venus":
        return ()
    if planet2 == "Mars":
        return ()
    if planet2 == "Jupiter":
        
