
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
    orbit_list = []
    orbit_list.append(planet1)
    orbit_list.append(planet2)

    for i in orbit_list:
        if i =="Mercury":
            orbit_list.append("Venus")
            orbit_list.append("Earth")
            orbit_list.append("Mars")
            orbit_list.append("Jupiter")
            orbit_list.append("Saturn")
            orbit_list.append("Uranus")
            orbit_list.append("Neptune")
        elif i =="Venus":
            orbit_list.append("Earth")
            orbit_list.append("Mars")
            orbit_list.append("Jupiter")
            orbit_list.append("Saturn")
            orbit_list.append("Uranus")
            orbit_list.append("Neptune")
        elif i =="Earth":
            orbit_list.append("Mars")
            orbit_list.append("Jupiter")
            orbit_list.append("Saturn")
            orbit_list.append("Uranus")
            orbit_list.append("Neptune")
        elif i =="Mars":
            orbit_list.append("Jupiter")
            orbit_list.append("Saturn")
            orbit_list.append("Uranus")
            orbit_list.append("Neptune")
        elif i =="Jupiter":
            orbit_list.append("Saturn")
            orbit_list.append("Uranus")
            orbit_list.append("Neptune")
        elif i =="Saturn":
            orbit_list.append("Uranus")
            orbit_list.append("Neptune")
        elif i =="Uranus":
            orbit_list.append("Neptune")


    return tuple(orbit_list)

