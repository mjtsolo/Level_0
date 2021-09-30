time = 67.345
hours = int(time)
minutes = (time*60) % 60
seconds = (time*3600) % 60
print("%d:%02d.%02d" % (hours, minutes, seconds))