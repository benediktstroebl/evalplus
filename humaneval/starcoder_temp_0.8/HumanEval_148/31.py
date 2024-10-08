
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
    assert type(planet1) == str and type(planet2) == str, "The input has to be strings"
    planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    # We have to set boundaries for every planet to choose from
    if planet1 not in planet_list or planet2 not in planet_list:
        return ()
    else:
        planet_list.remove(planet1)
        planet_list.remove(planet2)
        # We have to choose the boundaries
        if planet1 == "Mercury":
            if planet2 == "Venus":
                return ("Venus", "Earth")
            elif planet2 == "Earth":
                return ("Earth", "Mars")
            elif planet2 == "Mars":
                return ("Mars", "Jupiter")
            elif planet2 == "Jupiter":
                return ("Jupiter", "Saturn")
            elif planet2 == "Saturn":
                return ("Saturn", "Uranus")
            elif planet2 == "Uranus":
                return ("Uranus", "Neptune")
            elif planet2 == "Neptune":
                return ()
        elif planet1 == "Venus":
            if planet2 == "Earth":
                return ("Earth", "Mars")
            elif planet2 == "Mars":
                return ("Mars", "Jupiter")
            elif planet2 == "Jupiter":
                return ("Jupiter", "Saturn")
            elif planet2 == "Saturn":
                return ("Saturn", "Uranus")
            elif planet2 == "Uranus":
                return ("Uranus", "Neptune")
            elif planet2 == "Neptune":
                return ()
        elif planet1 == "Earth":
            if planet2 == "Mars":
                return ("Mars", "Jupiter")
            elif planet2 == "Jupiter":
                return ("Jupiter", "Saturn")
            elif planet2 == "Saturn":
                return ("Saturn", "Uranus")
            elif planet2 == "Uranus":
                return ("Uranus", "Neptune")
            elif planet2 == "Neptune":
                return ()
        elif planet1 == "Mars":
            if planet2 == "Jupiter":
                return ("Jupiter", "Sat
