service_cls= [
	"positioning",
	"networking",
	"rendering",
	"capturing",
	"object transfer",
	"audio",
	"telephony",
	"information"
]

major_cls = [
	"miscellaneous",
	"computer",
	"phone",
	"access point",
	"audio/video",
	"peripheral",
	"imaging",
	"wearable",
	"toy",
	"uncategorized"
]

computer_minor_cls = [
	"uncategorized",
	"desktop",
	"server",
	"laptop",
	"handheld",
	"palm",
	"wearable"
]

phone_minor_cls = [
	"uncategorized",
	"cellular",
	"cordless",
	"smart phone",
	"modem",
	"isdn"
]

access_point_minor_cls = [
	"fully",
	"1-17 percent",
	"17-33 percent",
	"33-50 percent",
	"50-67 percent",
	"67-83 percent",
	"83-99 percent",
	"not available"
]

audio_video_minor_cls = [
	"uncategorized",
	"headset",
	"handsfree",
	"unknown",
	"microphone",
	"loudspeaker",
	"headphones",
	"portable audio",
	"car audio",
	"set-top box",
	"hifi audio",
	"vcr",
	"video camera",
	"camcorder",
	"video monitor",
	"video display and loudspeaker",
	"video conferencing",
	"unknown",
	"gaming/toy"
]

peripheral_minor_cls = [
	"uncategorized",
	"keyboard",
	"pointing",
	"combo"
]


imaging_minor_cls = [
	"display",
	"camera",
	"scanner",
	"printer"
]

wearable_minor_cls = [
	"wrist watch",
	"pager",
	"jacket",
	"helmet",
	"glasses"
]

toy_minor_cls = [
	"robot",
	"vehicle",
	"doll",
	"controller",
	"game"
]

def get_major_class(klass):
	index = (klass >> 8) & 0x1F
	
	if index > 8:
		return major_cls[9]
	
	return major_cls[index]


def get_minor_class(klass):
	i = (klass >> 8) & 0x1F
	
	

	if i == 1: 
		minor_index = (klass >> 2) & 0x3F;
		if minor_index < len(computer_minor_cls):
			return computer_minor_cls[minor_index]
		else:
			return ""
	elif i == 2:
		minor_index = (klass >> 2) & 0x3F;
		if (minor_index < len(phone_minor_cls)):
			return phone_minor_cls[minor_index];
		return "";
	elif i == 3:
		minor_index = (klass >> 5) & 0x07;
		if (minor_index < len(access_point_minor_cls)):
			return access_point_minor_cls[minor_index]
		else:
			return "";
	elif i == 4: 
		minor_index = (klass >> 2) & 0x3F;
		if (minor_index < len(audio_video_minor_cls)):
			return audio_video_minor_cls[minor_index];
		else:
			return "";
	elif i == 5:
		minor_index = (klass >> 6) & 0x03;
		if (minor_index < len(peripheral_minor_cls)):
			return peripheral_minor_cls[minor_index];
		else:
			return "";
	elif i == 6:
		return imaging
		
	elif i == 7:
		minor_index = (klass >> 2) & 0x3F;
		if (minor_index < len(wearable_minor_cls)):
			return wearable_minor_cls[minor_index];
		else:
			return "";
	elif i == 8:
		minor_index = (klass >> 2) & 0x3F;
		if (minor_index < len(toy_minor_cls)):
			return toy_minor_cls[minor_index];
		else:
			return "";

	return "";
		
	
	
	
	
	
	
