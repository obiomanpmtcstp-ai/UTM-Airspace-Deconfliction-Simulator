# UTM Airspace Deconfliction Simulator

**Author/Candidate:** Anyanwu Obioma Anselam  
**Project Framework:** Satellite-Augmented Unmanned Traffic Management (UTM) & Automated Airspace Deconfliction (AAD)  
**Development Environment:** Visual Studio Code / Brackets

---

## 📋 Project Overview

This project demonstrates a dynamic adaptive safety scaling solution for satellite-augmented Unmanned Traffic Management systems operating under severe network degradation (40% packet loss). The core innovation is the **1.45x dynamic scaling multiplier** that expands the Cylindrical Volume Exclusion (CVE) safety radius to compensate for network latency.

### Key Components

#### 1. **Interactive Visual Simulation** (`Anyanwu_Obioma_Anselam_UTM_Airspace_Deconfliction_Simulator.html`)
A fully self-contained frontend application featuring:
- **Real-time 2D canvas visualization** of two UAVs with dynamic safety envelopes
- **Three operational modes:**
  - **Mode 1:** Ideal State (0% packet loss) - Green status, perfect tracking
  - **Mode 2:** Infrastructure Lag (40% packet loss) - Red/warning status, demonstrates breach vulnerability
  - **Mode 3:** Adaptive Override (1.45x multiplier) - Blue status, expanded CVE radius prevents collisions
- **Live metrics display:** Packet drop rate, CVE safety cushion, system status
- **Dark theme UI** optimized for thesis presentations

#### 2. **Algorithmic Backend** (`Anyanwu_Obioma_Anselam_Packet_Loss_Adaptive_Deconfliction.py`)
A pure Python implementation computing:
- Baseline CVE radius calculations (50 meters)
- Network degradation detection
- 1.45x adaptive multiplier application
- Dynamic radius expansion logic

---

## 🚀 Quick Start

### Option A: Run in VS Code with Live Server
1. Install the **Live Server** extension in VS Code
2. Right-click `Anyanwu_Obioma_Anselam_UTM_Airspace_Deconfliction_Simulator.html`
3. Select **Open with Live Server**
4. Simulator launches in your browser with live reload

### Option B: Run in Brackets
1. Open Brackets
2. File → Open Folder → Select this repository
3. Open the `.html` file
4. Click the **Live Preview** button (lightning icon)

### Option C: Run Python Backend
```bash
python Anyanwu_Obioma_Anselam_Packet_Loss_Adaptive_Deconfliction.py
```

---

## 🎯 How the Simulator Works

### Visual Flow:
1. **Click Tab 1 (Ideal State):** Watch UAV-Alpha and UAV-Beta move smoothly across the canvas with **50m green safety envelopes** — both drones tracked perfectly by satellite telemetry.

2. **Click Tab 2 (Infrastructure Lag):** Observe **network lag artifacts** — drones flicker between their real position (gray ghost dot) and displayed position (colored dot), simulating packet drops. The 50m envelope is **insufficient** — collision risk at center crossing.

3. **Click Tab 3 (Adaptive Override):** The system deploys the **1.45x multiplier**, expanding the CVE radius to **72.5 meters**. Drones are displayed with larger safety envelopes that **safely separate despite network lag**.

### Mathematical Foundation:
```
Base CVE Radius = 50.0 meters (ideal environment)
Packet Loss Threshold = 40%
Adaptive Multiplier = 1.45x

Adaptive Radius = 50.0 × 1.45 = 72.5 meters
Safety Margin Gained = 22.5 meters additional cushion
```

---

## 📊 Key Metrics

| Metric | Ideal | Failure | Override |
|--------|-------|---------|----------|
| **Packet Loss** | 0% | 40% | 40% |
| **CVE Radius** | 50m | 50m | 72.5m |
| **Safety Status** | ✅ NOMINAL | ❌ CRITICAL BREACH | ✅ ADAPTIVE ACTIVE |
| **Network Visibility** | Perfect | Degraded | Compensated |

---

## 🔬 Thesis Application

This simulator provides visual evidence for:
- **Problem Statement:** Satellite UTM systems fail under realistic network conditions (40% packet loss in Nigerian airspace)
- **Proposed Solution:** Dynamic CVE scaling adapts safety boundaries to compensate for latency
- **Validation:** The 1.45x multiplier prevents collisions while maintaining operational efficiency
- **Defense Presentation:** Interactive demo showing before/after scenarios

---

## 📁 File Structure

```
UTM-Airspace-Deconfliction-Simulator/
├── Anyanwu_Obioma_Anselam_UTM_Airspace_Deconfliction_Simulator.html
├── Anyanwu_Obioma_Anselam_Packet_Loss_Adaptive_Deconfliction.py
├── README.md (this file)
└── simulation_logs/ (optional: for CSV test data)
```

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, Canvas API (2D graphics)
- **Backend:** Python 3.x
- **Visualization:** Real-time animation with `requestAnimationFrame`
- **Algorithms:** Dynamic scaling, safety envelope mathematics

---

## 💡 Future Enhancements

- [ ] 3D visualization with Three.js
- [ ] Real satellite TLE data integration
- [ ] Multi-UAV (>2 aircraft) scenarios
- [ ] Configurable packet loss profiles
- [ ] CSV logging of simulation runs
- [ ] Network latency simulator
- [ ] Geofencing boundaries

---

## 📜 License

This project is part of an academic thesis and is provided as-is for educational purposes.

---

## ✉️ Contact

**Candidate:** Anyanwu Obioma Anselam  
**Project:** Satellite-Augmented UTM with Automated Airspace Deconfliction  
**Institution:** [Your University]  

---

*Last Updated: 2026-09-13*