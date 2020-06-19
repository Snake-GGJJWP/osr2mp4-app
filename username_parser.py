import glob
import io
import os, json
import configparser

settings = {
	"CursorSize" : "",
	"ShowInterface": "",
	"ScoreboardVisible": "",
	"DimLevel": "",
	"KeyOverlay": "",
	"AutomaticCursorSizing": "",
	"ScoreMeterScale": "",
	"VolumeMusic": "",
	"VolumeEffect": "",
	"IgnoreBeatmapSamples": "",
	"SkinSamples": ""
}


def read_properties_file(file_path):
	with open(file_path) as f:
		config = io.StringIO()
		config.write('[dummy_section]\n')
		config.write(f.read().replace('%', '%%'))
		config.seek(0, os.SEEK_SET)

		cp = configparser.ConfigParser()
		cp.readfp(config)

		return dict(cp.items('dummy_section'))


def get_configInfo(path):
	settings_result = []
	if path != "":
		cfg = glob.glob(path + "/*.cfg")
		props = read_properties_file(cfg[1])
		for x in settings:
			settings_result.append(props[x.lower()])
	return settings_result

