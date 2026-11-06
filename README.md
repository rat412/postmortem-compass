# Postmortem Compass

> 一个不追责（blameless）的故障复盘向导 Skill：把事故后的混乱信息整理成结构化、可落地、能真正防止复发的复盘报告。
> A blameless incident postmortem guide skill: turns post-incident chaos into a structured, actionable report that actually prevents recurrence.

## 定位 / Why

通用做法：让 AI「总结一下这次故障」—— 得到一篇平铺直叙的流水账，根因停在导火索，改进项是"加强监控、提高警惕"式的口号，复盘完无人执行。

本方案：以五阶段流程（收集 → 时间线 → 定级 → 根因 → 改进项）+ 事实/推断标注 + 三层归因（导火索/根因/放大因素）+ 改进项四象限（检测/预防/缓解/流程）+ 发布前质检清单，保证每份复盘不追责、可验收、能闭环。

Generic approach: ask an AI to "summarize the incident" — you get a flat narrative where the trigger passes as the root cause and action items are slogans nobody executes.

This skill: a five-phase workflow (collect → timeline → severity → root cause → action items) with fact/inference tagging, three-layer attribution (trigger / root cause / contributing factors), a four-quadrant action-item model, and a pre-delivery quality checklist — so every postmortem is blameless, verifiable, and closed-loop.

## 使用方式 / Usage

将本目录放入你的 Agent 技能目录（如 `~/.claude/skills/` 或项目 `.claude/skills/`），然后直接说人话触发：

Drop this folder into your agent's skills directory (e.g. `~/.claude/skills/` or a project-level skills folder), then just ask naturally:

```
帮我复盘一下昨晚支付接口超时的事故，这是告警截图和群聊记录……
Write a postmortem for last night's payment API timeout. Here are the alerts and chat log…
检查这份复盘报告写得合不合格
Review this postmortem against the quality checklist
```

Or scaffold a new report from the template (stdlib only, no dependencies):

```bash
python3 scripts/new_postmortem.py --title "Payment API outage" --sev SEV2 --date 2026-11-06
```

## 目录结构 / Structure

```
postmortem-compass/
├── SKILL.md                          # 技能入口：原则 + 五阶段流程 + 红线
├── README.md                         # 本文件
├── references/                       # 按需加载的参考知识
│   ├── blameless-culture.md          # 不追责文化的语言改写规则
│   ├── severity-levels.md            # SEV0–SEV4 定级标准与影响量化
│   └── root-cause-methods.md         # 5-Whys 与鱼骨图操作指南
├── checklists/
│   └── postmortem-quality-checklist.md  # 交付前质检清单（逐项过）
├── templates/
│   ├── postmortem-template.md        # 完整复盘报告模板
│   ├── timeline-template.md          # 时间线表模板
│   └── action-items-template.md      # 改进项跟踪表模板
├── examples/
│   └── example-postmortem.md         # 一份达标的完整示例（虚构场景）
└── scripts/
    └── new_postmortem.py             # 从模板生成新报告骨架（仅标准库）
```

## 流程概览 / Workflow at a glance

| Phase | 输出 | 通过门槛 |
|---|---|---|
| 0 收集 | 材料清单 + 缺口列表 | 时间戳统一时区 |
| 1 时间线 | 带 [FACT]/[INFER] 标注的时序表 | 无超检出目标的空窗 |
| 2 定级 | SEV 等级 + 量化影响面 | 影响有数字 |
| 3 根因 | 导火索/根因/放大因素三层分离 | 根因句无人名 |
| 4 改进项 | owner/deadline/验收标准齐备的清单 | 覆盖检测/预防/缓解/流程 |
| 5 成文质检 | 可发布的复盘报告 | 质检清单全绿 |

## 关键词 / Keywords

postmortem, incident review, blameless, root cause analysis, RCA, 5-whys, fishbone,
severity, SEV, action items, site reliability, SRE, outage,
故障复盘, 事故报告, 事后总结, 根因分析, 不追责, 时间线, 改进项, 运维, 稳定性
