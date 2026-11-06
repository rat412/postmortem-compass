---
name: postmortem-compass
description: >-
  Guide blameless incident postmortems / 故障复盘向导。Use when writing, reviewing or
  improving an incident review / postmortem / retrospective after an outage, incident,
  SEV, or production failure — 写故障复盘、事故报告、事后总结、根因分析、RCA、复盘改进项时使用。
  Builds timelines, runs root-cause analysis (5-Whys / fishbone), classifies severity,
  tracks action items to closure, and quality-checks the report.
---

# Postmortem Compass — 故障复盘向导

Turn raw incident chaos (chat logs, alerts, deploy records) into a blameless,
actionable postmortem that actually prevents recurrence.
把事故后的混乱信息（群聊记录、告警、变更记录）整理成一份不追责、可落地、能真正防止复发的复盘报告。

## Core principles 核心原则

1. **Blameless 不追责** — analyze systems and processes, never name individuals as the
   cause. "The deploy pipeline allowed X" not "Bob broke X".
2. **Timeline before cause 先时间线后归因** — establish agreed facts before any
   hypothesizing. Never let conclusions contaminate the chronology.
3. **Root cause, not trigger 挖根因不止于导火索** — the deploy that broke prod is the
   trigger, not the root cause. Keep asking why.
4. **Action items are deliverables 改进项必须可验收** — every action has an owner, a
   deadline, and a verifiable done-state. "Improve monitoring" is banned;
   "Add alert: p99 latency > 2s for 5min → page on-call" is accepted.
5. **A postmortem that nobody reads is waste 复盘要让人读得下去** — executive summary
   first, details after. One page of signal beats ten pages of noise.

## Workflow 工作流程

Follow these phases in order. Do not skip a gate.

### Phase 0 — Collect 收集原始材料
- Gather: alert timestamps, monitoring graphs, deploy/config-change records, chat
  threads, customer-impact reports.
- Note the timezone of every timestamp; convert all to one reference timezone.
- If materials are missing, list the gaps explicitly instead of guessing.

### Phase 1 — Timeline 重建时间线
- Use `templates/timeline-template.md`.
- Record: detection → diagnosis → mitigation → resolution, plus key context events
  (deploys, traffic changes) before detection.
- Mark each entry as **[FACT]** (verified) or **[INFER]** (inferred).
- Gate: timeline has no gaps longer than the detection target and every mitigation
  step has an observed effect recorded.

### Phase 2 — Severity & Impact 定级与影响面
- Classify with `references/severity-levels.md`.
- Quantify impact: duration, affected users/requests/revenue, data loss (if any).

### Phase 3 — Root cause 根因分析
- Use `references/root-cause-methods.md`: 5-Whys by default; fishbone categories
  (people / process / tooling / environment) for complex incidents.
- Separate: **trigger** (what set it off), **root cause** (why the system allowed it),
  **contributing factors** (what made it worse).
- Red flag: if the root cause sentence contains a person's name, rewrite it.

### Phase 4 — Action items 改进项
- Use `templates/action-items-template.md`.
- Each item: owner, deadline, priority (P0 before next similar risk window,
  P1 this sprint/quarter, P2 backlog), done-criteria.
- Cover four classes: detection, prevention, mitigation, process.

### Phase 5 — Write & quality-check 成文与质检
- Assemble with `templates/postmortem-template.md`.
- Run every item in `checklists/postmortem-quality-checklist.md`; fix failures
  before delivering.
- `examples/example-postmortem.md` shows a complete, passing example.

## Helper script

`scripts/new_postmortem.py` scaffolds a fresh postmortem file from the template
(stdlib only). Usage:

```bash
python3 scripts/new_postmortem.py --title "Payment API outage" --sev SEV2 --date 2026-11-06
```

## Banned patterns 反模式（红线）

- ❌ Naming a person as a cause anywhere in the report.
- ❌ "Human error" as a root cause — it is the start of the question, not the answer.
- ❌ Action items without owner/deadline/done-criteria.
- ❌ Copying chat logs verbatim into the report — distill, don't dump.
- ❌ Writing the conclusion first and cherry-picking timeline facts to fit it.
