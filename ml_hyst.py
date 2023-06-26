#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.3),
    on June 24, 2019, at 16:21
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import glob

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.3'
expName = 'Muller-Lyer'  # from the Builder filename that created this script
expInfo = {'session': '01', 'participant': '', 'span':'', 'order':''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\lpzdb\\pavloviaDemos\\stroop\\stroop.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text='INSTRUCTIONS\n\nFor each image, decide whether you could pick it up with one hand.\nPress any key to continue',
    font='Arial',
    units='height', pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
line = visual.Rect(
    win=win, name='line',units='cm', 
    width=10, height=0.2,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
hash1 = visual.Line(
    win=win, name='hash1', units='cm',
    start=(0, 0), end=(-2,2),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
hash2 = visual.Line(
    win=win, name='hash2', units='cm',
    start=(0, 0), end=(-2,-2),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
hash3 = visual.Line(
    win=win, name='hash3', units='cm',
    start=(0, 0), end=(2,2),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
hash4 = visual.Line(
    win=win, name='hash4', units='cm',
    start=(0, 0), end=(2,-2),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
routineText = visual.TextStim(win=win, name='thanksText',
    text='Could you pick this up with one hand?\n\n<Yes | No>',
    font='Arial',
    units='height', pos=[-0.5, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='Arial',
    units='height', pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready = keyboard.Keyboard()
# keep track of which components have finished
instructComponents = [instrText, ready]
for thisComponent in instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # not accounting for scr refresh
        instrText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *ready* updates
    waitOnFlip = False
    if t >= 0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t  # not accounting for scr refresh
        ready.frameNStart = frameN  # exact frame index
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready.status == STARTED and not waitOnFlip:
        theseKeys = ready.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# get the order from the experiment start and use it as an index for selecting the correct ordering of trials
orderfiles = glob.glob('*.xlsx')

# set up handler to look after randomisation of conditions etc

order_int = int(expInfo['order'])

trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(orderfiles[order_int]),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    line.setSize([width1,height1])

# "Shorter" arrangement is -1
    hash1.setEnd([hash_direction*2,2])
    hash2.setEnd([hash_direction*2,-2])
    hash3.setEnd([hash_direction*-2,2])
    hash4.setEnd([hash_direction*-2,-2])
    hash1.setPos([-width1/2,height1/2])
    hash2.setPos([-width1/2,-height1/2])
    hash3.setPos([width1/2,height1/2])
    hash4.setPos([width1/2,-height1/2])

    # line and hash parameters for each repeat
    #hash1.setOri(orientation)
    #hash1.setPos([0.02*width1,.01*height1])
    #word.setColor(letterColor, colorSpace='rgb')
    #word.setText(text)
    resp = keyboard.Keyboard()
    # keep track of which components have finished
    trialComponents = [line, hash1, hash2, hash3,hash4,routineText, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *line* updates
        if t >= 0.5 and line.status == NOT_STARTED:
            # keep track of start time/frame for later
            line.tStart = t  # not accounting for scr refresh
            line.frameNStart = frameN  # exact frame index
            #line.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
            line.setAutoDraw(True)
        # *hash1* updates
        if t >= 0.5 and hash1.status == NOT_STARTED:
            # keep track of start time/frame for later
            hash1.tStart = t  # not accounting for scr refresh
            hash1.frameNStart = frameN  # exact frame index
            #hash1.timeOnFlip(hash1, 'tStartRefresh')  # time at next scr refresh
            hash1.setAutoDraw(True)
        # *hash2* updates
        if t >= 0.5 and hash2.status == NOT_STARTED:
            # keep track of start time/frame for later
            hash2.tStart = t  # not accounting for scr refresh
            hash2.frameNStart = frameN  # exact frame index
            #hash1.timeOnFlip(hash1, 'tStartRefresh')  # time at next scr refresh
            hash2.setAutoDraw(True)
        # *hash3* updates
        if t >= 0.5 and hash3.status == NOT_STARTED:
            # keep track of start time/frame for later
            hash3.tStart = t  # not accounting for scr refresh
            hash3.frameNStart = frameN  # exact frame index
            #hash1.timeOnFlip(hash1, 'tStartRefresh')  # time at next scr refresh
            hash3.setAutoDraw(True)
        # *hash4* updates
        if t >= 0.5 and hash4.status == NOT_STARTED:
            # keep track of start time/frame for later
            hash4.tStart = t  # not accounting for scr refresh
            hash4.frameNStart = frameN  # exact frame index
            #hash1.timeOnFlip(hash1, 'tStartRefresh')  # time at next scr refresh
            hash4.setAutoDraw(True)


        # *resp* updates
        waitOnFlip = False
        if t >= 0.5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # not accounting for scr refresh
            resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp.keys = theseKeys.name  # just the last key pressed
                resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #trials.addData('line.started', word..tStartRefresh)
    #trials.addData('word.stopped', word.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    trials.addData('resp.keys',resp.keys)
    #trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t  # not accounting for scr refresh
        thanksText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        thanksText.tStop = t  # not accounting for scr refresh
        thanksText.frameNStop = frameN  # exact frame index
        win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksText.started', thanksText.tStartRefresh)
thisExp.addData('thanksText.stopped', thanksText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
