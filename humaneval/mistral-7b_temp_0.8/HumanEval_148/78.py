
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
    planet_list = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]

    # 1. Mercury ~ Neptune
    if planet1 in planet_list and planet2 in planet_list:
        if planet1 == "Mercury" and planet2 == "Neptune":
            return tuple(planet_list)

    # 2. Mercury ~ Mars
    if planet1 in planet_list and planet2 == "Mars":
        if planet1 == "Mercury":
            return tuple(planet_list[1:4])
        elif planet1 == "Venus":
            return tuple(planet_list[2:4])
        elif planet1 == "Earth":
            return tuple(planet_list[3:4])
        elif planet1 == "Mars":
            return ()

    # 3. Mercury ~ Jupiter
    if planet1 in planet_list
