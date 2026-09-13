# Setup Instructions for Anyanwu Obioma Anselam's UTM Simulator

## Prerequisites
- Visual Studio Code (recommended) OR Brackets
- Python 3.x (for backend script)
- Modern web browser (Chrome, Firefox, Safari, Edge)

---

## Method 1: VS Code with Live Server (Recommended)

### Step 1: Install Live Server Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Live Server"
4. Click **Install** on the extension by Ritwick Dey

### Step 2: Open the Repository
1. File → Open Folder
2. Navigate to and select the `UTM-Airspace-Deconfliction-Simulator` folder
3. Click **Select Folder**

### Step 3: Launch the Simulator
1. Right-click on `Anyanwu_Obioma_Anselam_UTM_Airspace_Deconfliction_Simulator.html`
2. Select **Open with Live Server**
3. Browser automatically opens to `http://localhost:5500`
4. Simulator loads with animated visualization

### Step 4: Interact with the Simulator
- **Tab 1:** Click to view ideal 0% packet loss scenario
- **Tab 2:** Click to view 40% packet loss with breach risks
- **Tab 3:** Click to view adaptive 1.45x override protection

---

## Method 2: Brackets with Live Preview

### Step 1: Open Brackets
1. Launch Brackets application

### Step 2: Open the Project
1. File → Open Folder
2. Select the `UTM-Airspace-Deconfliction-Simulator` folder

### Step 3: Launch Live Preview
1. Click the **Live Preview** button (lightning bolt icon ⚡) in the top-right
2. Browser opens with live preview
3. Any file changes auto-reload

### Step 4: Interact (same as Method 1, Step 4)

---

## Method 3: Direct Browser Opening (Offline)

1. Locate `Anyanwu_Obioma_Anselam_UTM_Airspace_Deconfliction_Simulator.html`
2. Right-click → **Open with** → Select your browser
3. Simulator displays (no live editing, but fully functional)

---

## Running the Python Backend Script

### Step 1: Open Terminal/Command Prompt

### Step 2: Navigate to Repository
```bash
cd path/to/UTM-Airspace-Deconfliction-Simulator
```

### Step 3: Run the Script
```bash
python Anyanwu_Obioma_Anselam_Packet_Loss_Adaptive_Deconfliction.py
```

### Expected Output:
```
--- Checking Airspace Safety Status [Author: Anyanwu O.A.] ---
Current Network Telemetry Link Packet Loss: 0%
Status: NOMINAL (Ideal Environment)
Assigned CVE Radius Protection Envelope: 50.0 meters

--- Checking Airspace Safety Status [Author: Anyanwu O.A.] ---
Current Network Telemetry Link Packet Loss: 40%
Warning: Severe Link Drop Detected (The Nigerian Factor Environmental Constraint)
Action: Deploying Dynamic Adaptive Safety Scaling Override Logic...
Status: ADAPTIVE COMPENSATION DEPLOYED
New Dynamic CVE Protection Radius: 72.5 meters (Expanded from 50.0m)
```

---

## Troubleshooting

### Issue: "Live Server port already in use"
**Solution:** 
- Change Live Server port in VS Code settings
- Or close other applications using port 5500

### Issue: Simulator doesn't animate
**Solution:**
- Ensure JavaScript is enabled in browser
- Try a different browser (Chrome recommended)
- Check browser console for errors (F12 → Console tab)

### Issue: Python script not found
**Solution:**
- Ensure you're in the correct directory
- Use full path: `python /path/to/script.py`
- Verify Python installation: `python --version`

### Issue: Canvas not rendering properly
**Solution:**
- Refresh browser (Ctrl+R or Cmd+R)
- Clear browser cache
- Try in incognito/private mode

---

## Features to Test

✅ **Ideal Mode (Tab 1)**
- Two drones smoothly moving left/right
- Green safety envelopes (50m radius)
- Status bar shows NOMINAL
- Packet loss: 0%

✅ **Failure Mode (Tab 2)**
- Network lag visualization (flickering drones)
- Gray "ghost" position vs colored actual position
- Red warning when drones get too close
- Packet loss: 40%
- CVE radius remains at 50m (insufficient)

✅ **Override Mode (Tab 3)**
- Blue safety envelopes (72.5m radius)
- Status bar shows ADAPTIVE ACTIVE
- Packet loss: 40%
- CVE radius expanded to 72.5m
- Drones never breach safety zones

---

## For Thesis Presentation

### Demo Script:
1. **Show Ideal:** "This is what perfect satellite telemetry looks like — real-time tracking with 50m safety."
2. **Show Failure:** "At 40% packet loss, the static boundary fails — drones breach before update."
3. **Show Override:** "Our 1.45x adaptive multiplier expands protection to 72.5m, safely compensating for lag."

### Performance Notes:
- Runs smoothly on most devices
- Animation frame rate: 60 FPS
- CPU usage: Minimal (<5%)
- Memory footprint: <20MB

---

## Support

For issues or customizations:
1. Check the README.md for overview
2. Review code comments in HTML/Python files
3. Verify all files are in the correct directory
4. Ensure file names match exactly (case-sensitive on Linux)

---

*Document created for Anyanwu Obioma Anselam's thesis project defense*