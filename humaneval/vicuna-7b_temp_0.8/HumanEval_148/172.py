
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
    if not planet1 or not planet2:
        return ()

    elif planet1 == "Mercury" and planet2 == "Mercury":
        return ("Mercury",)
    elif planet1 == "Venus" and planet2 == "Venus":
        return ("Venus",)
    elif planet1 == "Earth" and planet2 == "Earth":
        return ("Earth",)
    elif planet1 == "Mars" and planet2 == "Mars":
        return ("Mars",)
    elif planet1 == "Jupiter" and planet2 == "Jupiter":
        return ("Jupiter",)
    elif planet1 == "Saturn" and planet2 == "Saturn":
        return ("Saturn",)
    elif planet1 == "Uranus" and planet2 == "Uranus":
        return ("Uranus",)
    elif planet1 == "Neptune" and planet2 == "Neptune":
        return ("Neptune",)
    else:
        # sort the list of the planets according to their proximity to the sun
        sorted_list = sorted((
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1]),
            (planet1.split("/")[-1], planet2.split("/")[-1
