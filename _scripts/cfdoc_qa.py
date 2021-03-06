# The MIT License (MIT)
#
# Copyright (c) 2013 CFEngine AS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys

def OpenLogFile(config):
	logfile = open(config["log_file"], "a")
	return logfile

def LogProcessStart(config, string):
	logfile = OpenLogFile(config)
	logfile.write("\n")
	logfile.write("### %s\n" % string)
	logfile.write("\n")
	logfile.close()

def LogMissingDocumentation(config, element, strings, location):
	logfile = OpenLogFile(config)
	if not element.startswith("`"):
		element = "`%s`" % element
	logfile.write("* %s:\n" % element)
	if len(strings):
		logfile.write("    * Errors:\n")
	for string in strings:
		logfile.write("        * **%s**\n" % string)
	if len(location):
		logfile.write("    * Source location: `%s`\n" % location)
	logfile.write("    * Triggered by: `%s` (%d)\n" % (os.path.relpath(config["context_current_file"]), config["context_current_line_number"]))
	logfile.close()
