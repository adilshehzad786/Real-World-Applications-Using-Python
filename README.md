# Real-World-Applications-Using-Python


<h1>
  <h1>(Application 1)Teaching Kids Dictionary Online Compiler <h1>
  <li>https://Teaching-Kids-Dictionary.adilshehzad7.repl.run</li>
  
<h1>(Application 2) Live Volcano Map <h1>
  <li>https://volcano-map-live.adilshehzad7.repl.co</li>
  
  <h1> Use Python to Create Map  <h1>
  <li>https://repl.it/@AdilShehzad7/world-volcano-map-1</li>
  
   <h1>(Application 3) Website Blocker <h1>
  <li>https://repl.it/@AdilShehzad7/Python-Website-Blocker</li>
  
   <h1>(Application 4) Motion Dectector <h1>
  <li>https://repl.it/@AdilShehzad7/Webcam-Motion-Dectector</li>
  
  
  
  <div class="Box-body">
        <article class="markdown-body entry-content p-5" itemprop="text"><p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/4370926c1d11201e68c08e33d4fe6a06b89b2b1f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6164652532307769746825323025334333253230696e2d707974686f6e2d7265642e737667"><img src="https://camo.githubusercontent.com/4370926c1d11201e68c08e33d4fe6a06b89b2b1f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6164652532307769746825323025334333253230696e2d707974686f6e2d7265642e737667" alt="" data-canonical-src="https://img.shields.io/badge/Made%20with%20%3C3%20in-python-red.svg" style="max-width:100%;"></a></p>
<h1><a id="user-content-motion--detector-system--opencv" class="anchor" aria-hidden="true" href="#motion--detector-system--opencv"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="10" 
                                                                                                                                        ="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Motion- Detector System -OpenCV</h1>
<p>Python/OpenCV script that detect motion on webcam and allow record it to a file and plot a graph for proper Visualization.</p>
<h2><a id="user-content-description" class="anchor" aria-hidden="true" href="#description"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="10" height="10" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Description</h2>
<h3><a id="user-content-the-process" class="anchor" aria-hidden="true" href="#the-process"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="10" height="10" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The Process</h3>
<p>The trivial idea is to compute the difference between two frames apply a threshold the separate pixels that have changed from the others and then count all the black pixels. Then the average is calculated with this count and the total number of pixels and depending of the ceil the event is triggered or not.</p>
<h4><a id="user-content-additional-informations" class="anchor" aria-hidden="true" href="#additional-informations"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z">
</path></svg></a></h4><h2><a id="user-content-additional-informations" class="anchor" aria-hidden="true" href="#additional-informations"></a><a id="user-content-requirements" class="anchor" aria-hidden="true" href="#requirements"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="10" height="10" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Requirements</h2>
<ul>
<li>X86, X86_64, ARMv7 or ARMv8 version of Ubuntu 16.04 or Debian 8 (will most likely work on other Linux based operating systems as well)</li>
<li>Python 3.4 or above</li>
<li>Camera or Video file</li>
<li><a href="https://opencv.org/" rel="nofollow">Install OpenCV</a> or <code>pip install opencv-python</code></li>
<li><a href="https://bokeh.pydata.org/en/latest/" rel="nofollow">Install Bokeh library</a> or <code>pip install bokeh</code></li>
</ul>
Run Motion Detector
<p>Clone the repository and run the command <code>python plotting.py</code> in the project directory.</p>
Use case &amp; Future Scope
<ul>
<li>Motion Detector can be used on SBCs such as Raspberry Pi, NanoPi M1, CHIP, ODROID C1/C2/XU4, Pine A64, etc. to create compact smart cameras.</li>
<li>Threading and subprocess based architecture allows consistent FPS while processing frames, writing video files, moving files to remote location, etc. all concurrently.</li>
<li>Run multiple copies on a central server for IP based "dumb" cameras.</li>
<li>Supports several types of video inputs including USB and IP (wired/wireless) cameras, video files, etc.</li>
<li>Threshold based motion detection, ignore mask, multiple object marking and video recording.</li>
<li>Human feature detection with the ability to train your own detector.</li>
<li>Add your own plugins.</li>
</ul>
<p>Help me with a <g-emoji class="g-emoji" alias="star" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2b50.png">⭐️</g-emoji> if you like my work. <img class="emoji" title=":bowtie:" alt=":bowtie:" src="https://github.githubassets.com/images/icons/emoji/bowtie.png" height="10" width="10" align="absmiddle">
happy Coding ! <g-emoji class="g-emoji" alias="heart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png">❤️</g-emoji></p>
</article>
      </div>
  




  
 
