def deleteNone(d):

    #Delete keys with the value ``None`` in a dictionary, recursively.
    
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            deleteNone(value)
    return d 

def traverseLocation(x,loc):
    if(x in loc):
        return(loc[x])
    

def detailedAddress(location):
    address={
        'Village'           : (traverseLocation('village',location)),
        'Area'              : (traverseLocation('place_name',location)),
        'suburb'            : (traverseLocation('suburb',location)),
        'Tehsil'            : (traverseLocation('community_name',location)),
        'Tehsil'            : (traverseLocation('county',location)),
        'District'          : (traverseLocation('county_name',location)),
        'City'              : (traverseLocation('city',location)),
        'City District'     : (traverseLocation('city_district',location)),
        'State District'    : (traverseLocation('state_district',location)),
        'State'             : (traverseLocation('state',location)),
        'State'             : (traverseLocation('state_name',location)),
        'Country'           : (traverseLocation('country',location)),
        'Postal Code'       : (traverseLocation('postal_code',location)),
        'Postal Code'       : (traverseLocation('postcode',location))

    }
    return (deleteNone(address))