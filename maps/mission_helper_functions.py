
import sbs
from sbs_utils.procedural.query import to_object_list
from sbs_utils.procedural.roles import role
from sbs_utils.procedural.comms import comms_message
from math import atan2, tau


#**************************************************************************
def send_general_message(nName, textLine, face, srcID):

    sbs.send_story_dialog(0, nName, textLine, face, "#444")

    main_screen_client_list = to_object_list(role("mainscreen") & role("console"))

#    print(f"main screen client count = {len(main_screen_client_list)}")
    for c in main_screen_client_list:
        print(c.client_id)
        sbs.send_story_dialog(c.client_id, nName, textLine, face, "#444")

    # send it to all comms players as well
    my_players = to_object_list(role("__player__") & role("tsn"))
    for player in my_players:
        comms_message(textLine, srcID, player.id, face=face, from_name=nName)
#        COMMS_ORIGIN_ID=player.id
#        COMMS_SELECTED_ID=phoenix_id
#        << "{nName}"     
#            "{textLine}


#**************************************************************************
def round_off(floatNum):
    
    return round(floatNum)
    
#**************************************************************************
def int_conv(stringNum):
    
    return int(stringNum)

#**************************************************************************
def var_type(SomeVar):
    
    return type(SomeVar)

#**************************************************************************
def get_bearing_to(from_pos, to_pos):
    
    long_bearing = atan2(from_pos.x - to_pos.x, from_pos.z - to_pos.z) * 360 / tau + 180
    rounded_bearing = round(long_bearing)
    if rounded_bearing == 360:
        rounded_bearing = 0
    return rounded_bearing

#**************************************************************************
def round_to_nearest_200k(number):
    
    return round(number / 200000) * 200000

