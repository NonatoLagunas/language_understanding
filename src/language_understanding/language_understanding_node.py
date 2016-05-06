#!/usr/bin/env python
import rospy
import json
import std_msgs.msg
from planning_msgs.srv import *
import time
from pyrobotics import BB
from pyrobotics.parallel_senders import ParallelSender
from pyrobotics.messages import Command, Response
import egprs_interpreter

sentences = [
"bring me a chair from the studio",
"bring me a fork from the press",
"bring me a glass of water",
"bring me my book from the table",
"bring me my coat",
"bring me my telephone from the couch",
"bring me my towel",
"bring me my towel that is in the bathroom",
"bring me the bottle",
"bring me the cereals and the milk",
"bring me the cookie jar",
"bring me the glasses",
"bring me the pillow from the bed",
"bring me the red book",
"bring me the remote control",
"bring me the towel from the bathroom",
"bring me the towel from the drawer",
"bring me the wallet",
"bring me yogurt from the fridge",
"bring mug to bedroom",
"bring over the gray folder",
"bring slowly the box near the counter of the kitchen",
"bring the beers here and put them on the table next to the couch",
"bring the black book to the dining room",
"bring the book near the lamp",
"bring the cigarettes near the counter on the right",
"bring the fruit onto the dining table",
"bring the mug to the kitchen",
"bring the newspaper to the studio",
"bring the phone to the dinner table",
"bring the phone to the living room",
"bring the shampoo to the shower",
"bring the soap to the shower",
"bring the toilet paper to the bathroom",
"bring us some mustard",
"can you bring me my eyeglass you can find it on the table in the dining room",
"can you bring me my tablet",
"can you bring me the coke from the fridge",
"can you bring the glass to the sink",
"can you bring the mayo over here",
"can you bring the mug to the couch in the living room please",
"can you find a red t-shirt in the dresser",
"can you find the butcher knife",
"can you find the refrigerator for me",
"can you follow my mother to the garden",
"can you go over to the sofa",
"can you go to the bathroom please",
"can you go to the kitchen and bring me some bread from the pantry",
"can you go to the kitchen find a glass and bring it to me",
"can you grab my wine glass from the dining room",
"can you move a little bit to the right",
"can you place the mug to the head of the table",
"can you please bring my phone to the bathroom",
"can you please follow that guy over there",
"can you please go to the living room",
"can you please move near the right lamp",
"can you please search the book and bring it to me",
"can you please take out the garbage",
"can you put the detergent in the washing machine",
"can you put the soap in the washing machine",
"can you slowly follow my father",
"can you take the mug to the coffee table in the living room",
"can you turn the shower on",
"can you turn the taps in the shower on",
"carefully search for my wallet please",
"carry the book to my nightstand",
"carry the mug to the dining room",
"carry the phone to the chair",
"carry this mug to the bedstand",
"check if the stereo is on",
"check if there's clothes in the washing machine*",
"check main door status",
"check the answer machine for any messages",
"check the toilet paper",
"close the curatins in the living room",
"come with me",
"could you bring my water into the bedroom",
"could you close the shutters please",
"could you find a glass in the dining room",
"could you go to the bedroom and take the postcard on the nightstand please",
"could you hang my clothes on the cloth horse please",
"could you pick up the telephone",
"could you please bring us some water",
"could you please check if the coffee is ready",
"could you please go to the door",
"could you please move the trash bin from the kitchen to the studio",
"could you please move to the sink and open the cold water",
"could you please turn on the tv",
"could you put my clothes on the washing line please",
"could you put the vase on the coffee table",
"could you put the vase on the table please",
"could you switch on my laptop please",
"could you take the knife on the cutting board",
"could you turn on my pc",
"could you turn on the television please",
"deliver this message to the person in the living room",
"disconnect from the laptop at the right of the counter",
"do you think you can find my wallet",
"drive to kitchen",
"drive to the fridge",
"drop the pillow",
"drop the vase",
"fetch me the tissue box",
"find a bottle of water",
"find a magazine",
"find a plate",
"find me a cushion",
"find my keys",
"find my tablet",
"find the bottle of water and water the plant",
"find the glasses on the table",
"find the keys",
"find the lamp in the living room",
"find the magazine and put it on the table",
"find the phone",
"find the red pillow",
"find the refrigerator",
"find the remote control in the living room",
"find the towel",
"find the wallet",
"find the wine in the dining room",
"follow me",
"follow me carefully",
"follow me to the bathroom",
"follow me to the bedroom",
"follow me very fast",
"follow my friend into the living room",
"follow that person",
"follow the guy with the blue jacket",
"follow the man closely",
"follow the man in black",
"follow the person behind me",
"follow the person behind you",
"follow the person in front of me",
"follow the person in front of you",
"follow the person with the blond hair and the black pants fast",
"follow the person with the blonde hair and the black pants fast",
"follow this guy",
"get a fork from the drawer",
"get me my catalougue on the bedside table",
"get me my jacket",
"get me my towel",
"get my coat from the closet",
"get my computer from the seat",
"get the blue slippers from the bathroom",
"give me one apple from the table",
"give me the towel",
"go along with them",
"go close to the shower",
"go close to the table",
"go close to the window",
"go follow my sister around the house",
"go in front of the main door and open it",
"go in front of the poster",
"go in the bathroom and find the newspaper",
"go in the dining room and remove the tablecloth",
"go in the kitchen and switch off the coffee machine and the dishwasher",
"go near the fridge",
"go near the lamp",
"go near the window",
"go next to the door",
"go next to the tv set",
"go quickly to the corner and follow the skinny person",
"go straight to the living room",
"go to living room and turn on the tv",
"go to the bathroom",
"go to the bathroom take the rag go to the hall and clean the mirror",
"go to the bedroom",
"go to the coffee machine",
"go to the couch and bring me my laptop",
"go to the dining room",
"go to the dining room and take the glasses on the table",
"go to the dining room take all the plates from the table and put them in the dishwasher",
"go to the dining table",
"go to the fridge inside the kitchen",
"go to the garden",
"go to the kitchen",
"go to the laundry room",
"go to the living room and find a drink for me",
"go to the lounge",
"go to the right of the sofa",
"go to the sofa and search for the pillow",
"go to the telephone and check for any messages",
"grab the beer pack near the kitchen door",
"grab the book with the blue cover",
"grab the box on the left of the desktop",
"grab the cake plate",
"grab the key lanyard",
"grab this mug",
"hang my coat in the closet in my bedroom",
"hang this jacket in the closet of the corridor",
"hey robot follow john everywhere he goes and keep the same pace as he has",
"hey robot take the book and put it in the oven",
"i lost my ring in the living room can you search for it maybe it's near the sofa",
"i need my watch find it please",
"i need some toilet paper can you get me some",
"i need some utensils could you take me some",
"i need to turn on my computer in the studio",
"i really need you to bring me my aspirin it is in one of the drawers of the bathroom",
"i want some fruit bring me an apple or an orange",
"i want to go to sleep turn off the light",
"i want to jump in the shower can you turn it on",
"i want to wathc tv bring me the remote",
"i would like some beer can you grab one from the fridge and bring it here",
"i would like some cutlery can you get me some",
"i would like some loo roll can you get me some loo roll",
"i would like to read an architecture magazine can you bring me one",
"i'd really like to take a shower could you turn the shower on",
"i'm hungry go to the kitchen",
"i'm tired switch off the light please",
"in this room there are six chairs",
"john can you go to the bathroom to the down right cupboard and take a towel for me please thank you",
"john can you take the mug in the kitchen and bring it to the side of the bathtab please thanks",
"let go of the pack of beer",
"lets go get my book in the living room",
"lets go to the guest bedroom",
"lets go to the laundry room",
"lets take the soap to the kitchen",
"look for a blue book in the lounge",
"look for my mobile phone",
"look for the towel",
"michael carry me the phone that is on the glass table in the dining room",
"michael find my book on the sofa near the window",
"michael follow the guy with the red hoodie and the white shoes",
"michael go to the kitchen and get me some water",
"move along the wall",
"move away from the oven",
"move near the television of the kitchen",
"move next to the bed",
"move to bedroom",
"move to the bathroom",
"move to the bedroom",
"move to the dining room",
"move to the lamp on the right side of the bed",
"move to the left of the table",
"move to the living room",
"open the press",
"place the mug on the sink nearest to the refrigerator",
"please bring me the book to the bedroom",
"please bring the mug to the bedroom",
"please carry the mug to the bathroom",
"please close the blinds",
"please enter the bathroom and go towards the sink on the left hand side",
"please find me the black cushion which is on the bed",
"please find the flowers",
"please find the fruit",
"please find the lamp",
"please find the sunglasses",
"please find the toilet paper",
"please follow me",
"please follow me slowly",
"please follow me to the table",
"please follow the person in front of you",
"please go to the chair",
"please go to the mirror",
"please go to the sink",
"please go to the table",
"please move along the fences",
"please move to the far end of this table",
"please move to the fridge",
"please move to the front of the fridge",
"please open the pantry",
"please open the storage cupboard",
"please pick my mobile phone and put it on the chair near the table",
"please pick up the phone",
"please robot put the pan on the stove and control it",
"please take my trash to the laundry room",
"please take some pasta from the kitchen cabinet",
"put down the newspaper",
"put my clothes in the washing machine",
"put my jacket in the cabinet",
"put my jacket on the bed",
"put my mobile phone on the kitchen table",
"put th can in the trash",
"put the baking tray in the oven",
"put the book on the chair near the dining table",
"put the bottle in the bin",
"put the can in the bin",
"put the cell phone on the dining room table",
"put the coffee mug into the dishwasher",
"put the cup in the sink",
"put the glass in the sink",
"put the jacket in the wardrobe",
"put the kettle on the stove",
"put the milk in the fridge",
"put the mobile phone in the nightstand",
"put the mug in the living room",
"put the pillow on the bed",
"put the pillow on the chair",
"put the pillow under the bed",
"put the plate on the counter",
"put the soap on the bathroom sink",
"put this book on the bookshelf",
"put this pan on the stove",
"reboot the internet",
"release the bag",
"release the pot",
"restart the wifi",
"robot can you bring me a bath towel",
"robot can you bring me a magazine",
"robot can you bring me a towel",
"robot can you bring me my reading glasses from the bedroom",
"robot can you bring me the phone",
"robot can you bring me the telephone",
"robot can you bring the cornflakes box from the kitchen table",
"robot can you come to the studio with me",
"robot can you find a pack of napkins",
"robot can you fully lower the window blinds",
"robot can you get me a glass of water from the kitchen",
"robot can you open the cabinet",
"robot can you open the laundry room cabinet",
"robot can you open the washer",
"robot can you open the washing machine",
"robot can you pass me a plastic plate",
"robot can you pass me a plate",
"robot can you pass me the remote for the television",
"robot can you pass me the television remote",
"robot can you put the blinds all the way down",
"robot can you put the tv on",
"robot can you start my laptop computer",
"robot can you take me to the laundry room",
"robot can you turn my laptop on",
"robot can you turn the electring oven on",
"robot can you turn the oven on",
"robot can you turn the television on",
"robot carefully search the bedroom for my mobile phone",
"robot come with me to the living room",
"robot could you move near the table",
"robot follow me slowly",
"robot go get a book for me",
"robot go to the shower",
"robot i need you in the bathroom go there please",
"robot listen go into the bedroom and find the black pen it should be on the nightstand",
"robot please follow the postman",
"robot please search for the horn glasses",
"robot please take the mug to the sink",
"robot put this plate in the center of the table",
"robot this is the bedroom with a double bed with two lights next to it",
"robot why don't you go around and search for my hat",
"search for a blue plate",
"search for my tablet",
"search for the bottle of wine on the table",
"search for the coffee cups",
"search for the lamp",
"search for the scissors in the red drawer",
"search for the scissors they should be in the blue drawer",
"search for towel",
"search the living room for my mobile phone",
"search the living room for the remote control",
"see if the radio is on",
"see if the washing machine is empty",
"show me a snapshot of the food cooking on the stove",
"shut off the boiler",
"sit on one of the chairs of the table",
"sorry robot can you go to the kitchen and turn on the coffee machine",
"SQL_error",
"stop the tap",
"switch on the tv",
"take a coffee mug",
"take my cellphone to the bedroom",
"take my jacket from the jacket hook in my bedroom",
"take my phone and place it on the bench in the kitchen",
"take my phone into the living room",
"take my trousers on the bed and put them in the washing machine",
"take my wristwatch",
"take the apple jam jar",
"take the apple on the table",
"take the beer cans in the kitchen",
"take the black paperback from the bookshelf",
"take the bottle from the table and use it to water the plant",
"take the bottle of water on the table",
"take the bottle on the table",
"take the cereal box",
"take the coffee mugs from the kitchen cabinet and put them on the table",
"take the coke that is in the kitchen",
"take the corn can on the kitchen table",
"take the forks from the dishwasher",
"take the glass jar",
"take the jacket and bring it to me",
"take the knife with the black handle",
"take the magazine that is in the bathroom",
"take the mug to the bedroom",
"take the newspaper",
"take the newspaper from the stand and put it on the coffee table",
"take the orange juice from the fridge",
"take the remote control and turn on the tv",
"take the salt box",
"take the tablecloth in the drawer",
"take the tray to the bedroom",
"take three coffee cups and bring them to me",
"the bath-tub is on the left side",
"the fridge is on your right side",
"the keys should be on the table on the right of a pile of napkins",
"the living room is very light and bright",
"the sink is in the kitchen",
"the trash needs to go out could you take it out please",
"there are a lot of couches in the living room",
"there are some napkins on the kitchen table can you bring them here",
"there are some plastic bags in the kitchen drawer can you take one an bring it here",
"there are two abat jour next to the bed and seven pillows",
"there are two couches facing one another",
"there are two sinks in the kitchen",
"there is a bed with two lamps",
"there is a radio next to the bed",
"there is a table in the center of the dining room",
"there is some bread on the desk",
"there's a wristwatch on the couch side table can you bring it to me",
"there's a yellow jacket in the dining room can you bring it to me",
"this is a bathroom and there is towels on the right and a bath tub on the left",
"this is a bathroom where the door is on the right",
"this is a bathroom with a shower bath and double sink",
"this is a bed room",
"this is a bed room where we can find a bed and few pillows and two clops",
"this is a bedroom with big double bed and two bedside tables",
"this is a bedroom with one bed and two night stands",
"this is a double bedroom with four pictures on the wall",
"this is a living room with white furniture",
"this is a table with a glass deck",
"this is a very wide and bright livingroom",
"turn off the boiler",
"turn off the light and turn off the computer",
"turn off the tap",
"turn on the heating",
"turn on the light and go to the computer",
"turn on the television",
"turn on the thermostat",
"where is my gray binder",
"would you please bring me my phone from the bed room",
"would you please follow me to the kitchen",
"you are in a very big bathroom",
"you are in the bedroom and the bed is between two lamps",
"you should bring me the brown envelope that is on the table",
]


def process_string(request):
	#get the recognized string and send it to the reco function
	interpreted_command = egprs_interpreter.interpret_command(request.sentence)
	#convert the interpretation json-format to lists 
	jsonCFR = json.loads(interpreted_command)

	#send the response back
	response = parse_sentence_cfrResponse()
	response.cfr.command = jsonCFR["action"]
	for key in jsonCFR["params"].keys():
		response.cfr.frame_id.append(key)
		response.cfr.frame_value.append(jsonCFR["params"][key])
	return response

def main():
	rospy.init_node('language_understanding')
 	#f = open('interpretationResult', 'w')
	#count = 0
	#for sentence in sentences:
	#	f.write("\n----------------------------------------------------\n")
	#	f.write(str(("Sentence to interpret: ", sentence)))
	#	interpResult = egprs_interpreter.interpret_command(sentence)
	#	if interpResult != "NO_INTERPRETATION":
	#		count=count+1
	#	f.write(str("\n" + interpResult))
	#f.closed

	#print "Total interpreted: ", count

	#advertise a service to parsing
	rospy.Service('language_understanding/parse_sentence', parse_sentence_cfr, process_string)

	rospy.spin()

if __name__ == "__main__":
	main()
