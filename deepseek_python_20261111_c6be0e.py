<!DOCTYPE html>
<html lang="ru" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Инженерный дашборд · ООО «Дорожно-Строительное Управление №1» · Сводный отчёт</title>
<style>
    :root {
        --bg: #eef2f7;
        --bg-gradient:
            radial-gradient(1200px 600px at 10% -10%, #dbeafe 0%, transparent 60%),
            radial-gradient(1000px 500px at 110% 10%, #e0e7ff 0%, transparent 55%);
        --surface: #ffffff;
        --surface-2: #f8fafc;
        --surface-3: #f1f5f9;
        --border: #e2e8f0;
        --border-strong: #cbd5e1;
        --text: #0f172a;
        --text-muted: #64748b;
        --text-dim: #94a3b8;
        --primary: #2563eb;
        --primary-hover: #1d4ed8;
        --primary-soft: #eff6ff;
        --primary-border: #bfdbfe;
        --accent: #7c3aed;
        --success: #059669;
        --success-soft: #ecfdf5;
        --danger: #dc2626;
        --danger-soft: #fef2f2;
        --warning: #d97706;
        --warning-soft: #fffbeb;
        --shadow-sm: 0 1px 2px rgba(15, 23, 42, .06);
        --shadow: 0 1px 3px rgba(15, 23, 42, .08), 0 1px 2px rgba(15, 23, 42, .04);
        --shadow-lg: 0 10px 30px rgba(15, 23, 42, .10);
        --radius: 14px;
        --radius-sm: 9px;
        --ease: cubic-bezier(.22, .61, .36, 1);
    }
    html[data-theme="dark"] {
        --bg: #0a0f1a;
        --bg-gradient:
            radial-gradient(1200px 600px at 10% -10%, #1e293b 0%, transparent 55%),
            radial-gradient(1000px 500px at 110% 10%, #172554 0%, transparent 50%);
        --surface: #101828;
        --surface-2: #151f33;
        --surface-3: #1a2740;
        --border: #1f2d47;
        --border-strong: #2c3f60;
        --text: #e8eef9;
        --text-muted: #93a4bd;
        --text-dim: #5b6b85;
        --primary: #3b82f6;
        --primary-hover: #60a5fa;
        --primary-soft: #10203c;
        --primary-border: #1e3a8a;
        --accent: #a78bfa;
        --success: #10b981;
        --success-soft: #062b22;
        --danger: #f87171;
        --danger-soft: #2a1215;
        --warning: #fbbf24;
        --warning-soft: #2a1f0a;
        --shadow-sm: 0 1px 2px rgba(0, 0, 0, .4);
        --shadow: 0 1px 3px rgba(0, 0, 0, .5), 0 1px 2px rgba(0, 0, 0, .3);
        --shadow-lg: 0 10px 30px rgba(0, 0, 0, .55);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                     "Helvetica Neue", Arial, "Noto Sans", sans-serif;
        background: var(--bg);
        background-image: var(--bg-gradient);
        background-attachment: fixed;
        color: var(--text);
        line-height: 1.5;
        min-height: 100vh;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        transition: background-color .35s var(--ease), color .35s var(--ease);
    }
    .topbar {
        position: sticky; top: 0; z-index: 50;
        backdrop-filter: saturate(180%) blur(14px);
        -webkit-backdrop-filter: saturate(180%) blur(14px);
        background: color-mix(in srgb, var(--surface) 78%, transparent);
        border-bottom: 1px solid var(--border);
        transition: background .35s var(--ease), border-color .35s var(--ease);
    }
    .topbar__inner {
        max-width: 1280px; margin: 0 auto; padding: 14px 22px;
        display: flex; align-items: center; justify-content: space-between; gap: 16px;
    }
    .brand { display: flex; align-items: center; gap: 12px; min-width: 0; }
    .brand__logo {
        width: 40px; height: 40px; border-radius: 11px;
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        display: grid; place-items: center; color: #fff; flex-shrink: 0;
        box-shadow: 0 4px 14px rgba(37, 99, 235, .35);
    }
    .brand__logo svg { width: 22px; height: 22px; }
    .brand__text { min-width: 0; }
    .brand__title { font-size: 1.02rem; font-weight: 700; letter-spacing: -0.015em;
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .brand__subtitle { font-size: .74rem; color: var(--text-muted);
        letter-spacing: .02em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .theme-toggle {
        position: relative; width: 62px; height: 32px; border-radius: 999px;
        border: 1px solid var(--border-strong); background: var(--surface-3);
        cursor: pointer; flex-shrink: 0; padding: 0; outline: none;
        transition: background .3s var(--ease), border-color .3s var(--ease);
    }
    .theme-toggle:focus-visible { box-shadow: 0 0 0 3px var(--primary-soft), 0 0 0 4px var(--primary); }
    .theme-toggle__thumb {
        position: absolute; top: 2px; left: 2px; width: 26px; height: 26px;
        border-radius: 50%; background: var(--surface); box-shadow: var(--shadow);
        display: grid; place-items: center; color: var(--warning);
        transition: transform .35s var(--ease), background .3s var(--ease);
    }
    html[data-theme="dark"] .theme-toggle__thumb { transform: translateX(30px); color: #93c5fd; }
    .theme-toggle__thumb svg { width: 15px; height: 15px; }
    .theme-toggle__icon-sun, .theme-toggle__icon-moon {
        transition: opacity .25s var(--ease), transform .35s var(--ease);
    }
    html[data-theme="dark"] .theme-toggle__icon-sun {
        opacity: 0; transform: rotate(-90deg) scale(.5); position: absolute;
    }
    html:not([data-theme="dark"]) .theme-toggle__icon-moon {
        opacity: 0; transform: rotate(90deg) scale(.5); position: absolute;
    }
    .tabs-wrapper { max-width: 1280px; margin: 0 auto; padding: 22px 22px 0; }
    .tabs {
        display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; padding: 6px;
        background: var(--surface); border: 1px solid var(--border);
        border-radius: var(--radius); box-shadow: var(--shadow-sm);
        transition: background .35s var(--ease), border-color .35s var(--ease);
    }
    @media (max-width: 900px) { .tabs { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 560px) { .tabs { grid-template-columns: 1fr; } }
    .tab {
        position: relative; display: flex; align-items: center; gap: 12px;
        padding: 13px 16px; border: none; background: transparent;
        border-radius: var(--radius-sm); cursor: pointer; font-family: inherit;
        font-size: .9rem; font-weight: 600; color: var(--text-muted);
        text-align: left; outline: none;
        transition: background .25s var(--ease), color .25s var(--ease);
    }
    .tab:hover { background: var(--surface-3); color: var(--text); }
    .tab:focus-visible { box-shadow: 0 0 0 2px var(--primary); }
    .tab.is-active {
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        color: #fff; box-shadow: 0 4px 14px rgba(37, 99, 235, .35);
    }
    .tab__icon {
        width: 34px; height: 34px; flex-shrink: 0; border-radius: 9px;
        display: grid; place-items: center; background: var(--surface-3);
        color: var(--primary);
        transition: background .25s var(--ease), color .25s var(--ease);
    }
    .tab.is-active .tab__icon { background: rgba(255, 255, 255, .18); color: #fff; }
    .tab__icon svg { width: 18px; height: 18px; }
    .tab__label { display: flex; flex-direction: column; gap: 1px; min-width: 0; }
    .tab__num { font-size: .68rem; font-weight: 700; letter-spacing: .06em;
        text-transform: uppercase; opacity: .65; }
    .tab__name { font-size: .85rem; font-weight: 600; white-space: nowrap;
        overflow: hidden; text-overflow: ellipsis; }
    .main { max-width: 1280px; margin: 0 auto; padding: 22px; }
    .panel { display: none; animation: fadeIn .35s var(--ease); }
    .panel.is-active { display: block; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
    .panel-grid {
        display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
        gap: 22px; align-items: start;
    }
    @media (max-width: 1000px) { .panel-grid { grid-template-columns: 1fr; } }
    .card {
        background: var(--surface); border: 1px solid var(--border);
        border-radius: var(--radius); box-shadow: var(--shadow); padding: 24px;
        transition: background .35s var(--ease), border-color .35s var(--ease);
    }
    .card + .card { margin-top: 18px; }
    .card__title {
        display: flex; align-items: center; gap: 10px; font-size: 1rem;
        font-weight: 700; letter-spacing: -0.01em; padding-bottom: 16px;
        margin-bottom: 20px; border-bottom: 1px solid var(--border);
    }
    .card__title-icon {
        width: 30px; height: 30px; border-radius: 8px; background: var(--primary-soft);
        color: var(--primary); display: grid; place-items: center; flex-shrink: 0;
    }
    .card__title-icon svg { width: 16px; height: 16px; }
    .card__title-text { display: flex; flex-direction: column; gap: 1px; min-width: 0; }
    .card__title-main { font-size: .95rem; font-weight: 700; }
    .card__title-sub { font-size: .74rem; font-weight: 500; color: var(--text-muted); }
    .form-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
    @media (max-width: 520px) { .form-grid { grid-template-columns: 1fr; } }
    .field { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    .field--common {
        position: relative; padding: 12px; margin: -12px;
        background: linear-gradient(135deg,
            color-mix(in srgb, var(--warning) 10%, transparent) 0%,
            color-mix(in srgb, var(--warning) 4%, transparent) 100%);
        border: 1px dashed color-mix(in srgb, var(--warning) 45%, transparent);
        border-radius: var(--radius-sm);
    }
    .field__label {
        font-size: .78rem; font-weight: 600; color: var(--text-muted);
        letter-spacing: .01em; display: flex; align-items: center;
        justify-content: space-between; gap: 6px; flex-wrap: wrap;
    }
    .field__formula {
        font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
        font-size: .68rem; color: var(--text-dim); font-weight: 500;
        background: var(--surface-3); padding: 1px 6px; border-radius: 5px;
    }
    .field__badge {
        font-size: .62rem; font-weight: 700; letter-spacing: .06em;
        text-transform: uppercase; color: var(--warning);
        background: var(--warning-soft); padding: 2px 7px; border-radius: 5px;
        border: 1px solid color-mix(in srgb, var(--warning) 30%, transparent);
        white-space: nowrap;
    }
    .field__wrap { position: relative; display: flex; align-items: center; }
    .field__input {
        width: 100%; padding: 12px 54px 12px 14px; font-family: inherit;
        font-size: 1rem; font-weight: 500; color: var(--text);
        background: var(--surface-2); border: 1.5px solid var(--border);
        border-radius: var(--radius-sm); outline: none;
        font-variant-numeric: tabular-nums;
        transition: border-color .18s var(--ease), box-shadow .18s var(--ease),
                    background .18s var(--ease);
        -moz-appearance: textfield;
    }
    .field__input::-webkit-outer-spin-button,
    .field__input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
    .field__input:hover { border-color: var(--border-strong); }
    .field__input:focus {
        border-color: var(--primary); background: var(--surface);
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary) 18%, transparent);
    }
    .field__input.is-invalid { border-color: var(--danger); background: var(--danger-soft); }
    .field__input.is-invalid:focus {
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--danger) 20%, transparent);
    }
    .field__input.is-common { border-color: color-mix(in srgb, var(--warning) 55%, var(--border)); }
    .field__unit {
        position: absolute; right: 14px; font-size: .78rem; font-weight: 600;
        color: var(--text-dim); pointer-events: none;
    }
    .field__hint {
        font-size: .72rem; color: var(--text-dim); min-height: 15px;
        line-height: 1.35; transition: color .18s var(--ease);
    }
    .field__hint.is-error { color: var(--danger); font-weight: 600; }
    .results-stack { display: flex; flex-direction: column; gap: 14px; }
    .result-card {
        position: relative; overflow: hidden; border-radius: var(--radius);
        padding: 20px 22px; background: var(--surface-2);
        border: 1px solid var(--border); box-shadow: var(--shadow-sm);
        transition: transform .25s var(--ease), box-shadow .25s var(--ease),
                    background .35s var(--ease), border-color .35s var(--ease);
    }
    .result-card::before {
        content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px;
        background: var(--text-dim); opacity: .5;
        transition: background .3s var(--ease), opacity .3s var(--ease);
    }
    .result-card--primary {
        background: linear-gradient(135deg,
            color-mix(in srgb, var(--primary) 10%, var(--surface)) 0%,
            color-mix(in srgb, var(--primary) 4%, var(--surface)) 100%);
        border-color: var(--primary-border);
        box-shadow: 0 6px 22px color-mix(in srgb, var(--primary) 14%, transparent);
    }
    .result-card--primary::before {
        background: linear-gradient(180deg, var(--primary), var(--accent)); opacity: 1;
    }
    .result-card--accent::before {
        background: linear-gradient(180deg, var(--success), #059669); opacity: 1;
    }
    .result-card__label {
        display: flex; align-items: center; gap: 7px; font-size: .72rem;
        font-weight: 700; text-transform: uppercase; letter-spacing: .07em;
        color: var(--text-muted); margin-bottom: 8px;
    }
    .result-card__label svg { width: 13px; height: 13px; color: var(--text-dim); }
    .result-card--primary .result-card__label svg { color: var(--primary); }
    .result-card__value {
        font-size: clamp(1.85rem, 4vw, 2.4rem); font-weight: 800;
        letter-spacing: -0.03em; line-height: 1.05;
        font-variant-numeric: tabular-nums; word-break: break-word; color: var(--text);
    }
    .result-card--primary .result-card__value { color: var(--primary); }
    .result-card__unit {
        font-size: .95rem; font-weight: 600; color: var(--text-muted);
        margin-left: 6px; letter-spacing: 0;
    }
    .result-card__sub {
        font-size: .78rem; color: var(--text-muted); margin-top: 6px; line-height: 1.45;
    }
    .formula-block {
        margin-top: 18px; padding: 16px 18px; background: var(--surface-3);
        border-left: 3px solid var(--primary); border-radius: var(--radius-sm);
        font-size: .82rem; color: var(--text-muted); line-height: 1.75;
        transition: background .35s var(--ease), border-color .35s var(--ease);
    }
    .formula-block__title {
        font-size: .74rem; font-weight: 700; text-transform: uppercase;
        letter-spacing: .07em; color: var(--text); margin-bottom: 8px;
        display: flex; align-items: center; gap: 6px;
    }
    .formula-block__title svg { width: 13px; height: 13px; color: var(--primary); }
    .formula-block code {
        font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
        background: var(--surface); padding: 2px 7px; border-radius: 5px;
        font-size: .79rem; color: var(--text); border: 1px solid var(--border); font-weight: 600;
    }
    .formula-block em { font-style: normal; color: var(--primary); font-weight: 700; }
    .formula-block p + p { margin-top: 6px; }
    .transfer-block {
        margin-top: 18px; padding: 18px; border-radius: var(--radius);
        background: linear-gradient(135deg,
            color-mix(in srgb, var(--warning) 12%, var(--surface)) 0%,
            color-mix(in srgb, var(--warning) 4%, var(--surface)) 100%);
        border: 1px solid color-mix(in srgb, var(--warning) 35%, transparent);
        display: flex; flex-direction: column; gap: 12px;
    }
    .transfer-block__header {
        display: flex; align-items: center; gap: 10px; font-size: .85rem;
        font-weight: 700; color: var(--text);
    }
    .transfer-block__header-icon {
        width: 26px; height: 26px; border-radius: 7px; background: var(--warning-soft);
        color: var(--warning); display: grid; place-items: center; flex-shrink: 0;
    }
    .transfer-block__header-icon svg { width: 14px; height: 14px; }
    .transfer-block__desc { font-size: .78rem; color: var(--text-muted); line-height: 1.5; }
    .transfer-block__desc strong { color: var(--text); }
    .actions {
        display: flex; gap: 10px; flex-wrap: wrap; justify-content: flex-end;
        margin-top: 20px; padding-top: 20px; border-top: 1px solid var(--border);
    }
    .actions--transfer {
        border-top: none; padding-top: 0; margin-top: 0; justify-content: flex-start;
    }
    .btn {
        font-family: inherit; font-size: .86rem; font-weight: 600;
        padding: 11px 20px; border-radius: var(--radius-sm);
        border: 1.5px solid transparent; cursor: pointer;
        display: inline-flex; align-items: center; justify-content: center;
        gap: 7px; white-space: nowrap; line-height: 1; outline: none;
        transition: background .18s var(--ease), border-color .18s var(--ease),
                    color .18s var(--ease), transform .1s var(--ease),
                    box-shadow .18s var(--ease);
    }
    .btn:active { transform: translateY(1px); }
    .btn:focus-visible { box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary) 25%, transparent); }
    .btn svg { width: 15px; height: 15px; flex-shrink: 0; }
    .btn--primary {
        background: var(--primary); color: #fff;
        box-shadow: 0 3px 10px color-mix(in srgb, var(--primary) 35%, transparent);
    }
    .btn--primary:hover {
        background: var(--primary-hover);
        box-shadow: 0 5px 16px color-mix(in srgb, var(--primary) 40%, transparent);
    }
    .btn--secondary {
        background: var(--surface); color: var(--text); border-color: var(--border-strong);
    }
    .btn--secondary:hover {
        background: var(--surface-3); border-color: var(--primary); color: var(--primary);
    }
    .btn--ghost { background: transparent; color: var(--text-muted); border-color: var(--border); }
    .btn--ghost:hover { background: var(--surface-3); color: var(--text); }
    .btn--warning {
        background: var(--warning); color: #fff;
        box-shadow: 0 3px 10px color-mix(in srgb, var(--warning) 35%, transparent);
    }
    .btn--warning:hover {
        background: color-mix(in srgb, var(--warning) 88%, #000);
        box-shadow: 0 5px 16px color-mix(in srgb, var(--warning) 45%, transparent);
    }
    .btn--success {
        background: var(--success); color: #fff;
        box-shadow: 0 3px 10px color-mix(in srgb, var(--success) 35%, transparent);
    }
    .btn--success:hover {
        background: color-mix(in srgb, var(--success) 88%, #000);
        box-shadow: 0 5px 16px color-mix(in srgb, var(--success) 45%, transparent);
    }
    .btn--word {
        background: #2b579a; color: #fff;
        box-shadow: 0 3px 10px rgba(43, 87, 154, .35);
    }
    .btn--word:hover { background: #1f4374; box-shadow: 0 5px 16px rgba(43, 87, 154, .45); }
    @media (max-width: 520px) {
        .actions { flex-direction: column-reverse; align-items: stretch; }
        .btn { width: 100%; }
    }
    .report-actions {
        display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 22px;
        padding-bottom: 22px; border-bottom: 1px solid var(--border);
    }
    .report-document {
        background: #ffffff; color: #000000; padding: 32px 36px;
        border: 1px solid #000000;
        font-family: 'Times New Roman', 'Liberation Serif', Times, serif;
        font-size: 12pt; line-height: 1.45; box-shadow: var(--shadow-sm);
    }
    html[data-theme="dark"] .report-document { background: #f6f7f9; color: #000; }
    .report-doc__header {
        text-align: center; border-bottom: 2px solid #000; padding-bottom: 14px;
        margin-bottom: 20px; font-size: 11pt; line-height: 1.55;
    }
    .report-doc__header > div { margin: 2px 0; }
    .report-doc__org {
        font-weight: 700; font-size: 12pt; text-transform: uppercase;
        letter-spacing: .04em; margin-bottom: 4px !important;
    }
    .report-doc__title {
        text-align: center; font-size: 13pt; font-weight: 700;
        text-transform: uppercase; letter-spacing: .04em;
        margin: 18px 0 6px; line-height: 1.35;
    }
    .report-doc__date {
        text-align: right; font-size: 10pt; color: #333;
        font-style: italic; margin-bottom: 16px;
    }

    /* -------- Секции отчёта -------- */
    .report-doc__section {
        margin: 20px 0;
    }
    .report-doc__section-title {
        font-size: 11.5pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .04em;
        margin-bottom: 10px;
        padding-bottom: 5px;
        border-bottom: 1.5px solid #000;
    }

    /* -------- Таблица «1. Общие сведения» с полями ввода -------- */
    .report-doc__info-table {
        width: 100%;
        border-collapse: collapse;
        margin: 8px 0;
        font-size: 10.5pt;
    }
    .report-doc__info-table td {
        border: 1px solid #000;
        padding: 7px 10px;
        vertical-align: middle;
    }
    .report-doc__info-label {
        width: 32%;
        background: #f0f0f0;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 9.5pt;
        letter-spacing: .02em;
    }
    .report-doc__input {
        width: 100%;
        padding: 4px 6px;
        font-family: inherit;
        font-size: 10.5pt;
        font-weight: 600;
        color: #000;
        background: transparent;
        border: 1px solid transparent;
        border-bottom: 1px solid #666;
        border-radius: 0;
        outline: none;
        transition: background .15s, border-color .15s;
    }
    .report-doc__input:hover {
        background: #f5f8ff;
        border-bottom-color: #2563eb;
    }
    .report-doc__input:focus {
        background: #eef4ff;
        border-bottom: 1.5px solid #2563eb;
    }
    .report-doc__input::placeholder {
        color: #999;
        font-weight: 400;
        font-style: italic;
    }

    /* -------- Результаты -------- */
    .report-doc__table {
        width: 100%; border-collapse: collapse; margin: 10px 0 22px; font-size: 10.5pt;
    }
    .report-doc__table th,
    .report-doc__table td {
        border: 1px solid #000; padding: 5px 8px; text-align: left; vertical-align: top;
    }
    .report-doc__table th {
        background: #e8e8e8; font-weight: 700; font-size: 10pt;
        text-transform: uppercase; letter-spacing: .02em;
    }
    .report-doc__table td.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
    .report-doc__table tr.section-row td {
        background: #f0f0f0; font-weight: 700; text-transform: uppercase;
        font-size: 10pt; letter-spacing: .03em;
    }

    /* -------- Заключение -------- */
    .report-doc__conclusion {
        border: 1px solid #000;
        padding: 14px 18px;
        margin: 0;
    }
    .report-doc__conclusion p {
        font-size: 11pt; line-height: 1.6; text-align: justify; margin: 0;
    }

    /* -------- Подписи -------- */
    .report-doc__signature { margin-top: 36px; font-size: 11pt; line-height: 2; }
    .report-doc__signature-line {
        display: inline-block; border-bottom: 1px solid #000; min-width: 130px;
        height: 1em; margin: 0 8px; vertical-align: bottom;
    }
    .report-doc__mp { margin-top: 6px; font-size: 10pt; color: #333; }
    .report-doc__empty {
        text-align: center; padding: 48px 20px; color: #555;
        font-size: 11pt; font-style: italic;
    }

    .toast-container {
        position: fixed; top: 80px; right: 20px; z-index: 9999;
        display: flex; flex-direction: column; gap: 10px;
        pointer-events: none; max-width: calc(100vw - 40px);
    }
    .toast {
        padding: 12px 16px; background: var(--surface); color: var(--text);
        border: 1px solid var(--border); border-left: 3px solid var(--primary);
        border-radius: var(--radius-sm); box-shadow: var(--shadow-lg);
        font-size: .84rem; font-weight: 500; line-height: 1.45;
        animation: toastIn .35s var(--ease); pointer-events: auto;
        display: flex; align-items: flex-start; gap: 10px; max-width: 360px;
    }
    .toast svg { width: 16px; height: 16px; flex-shrink: 0; margin-top: 1px; }
    .toast--success { border-left-color: var(--success); }
    .toast--success svg { color: var(--success); }
    .toast--error { border-left-color: var(--danger); }
    .toast--error svg { color: var(--danger); }
    .toast--info { border-left-color: var(--primary); }
    .toast--info svg { color: var(--primary); }
    @keyframes toastIn { from { opacity: 0; transform: translateX(30px); } to { opacity: 1; transform: translateX(0); } }
    @keyframes toastOut { from { opacity: 1; transform: translateX(0); } to { opacity: 0; transform: translateX(30px); } }
    .toast.is-leaving { animation: toastOut .3s var(--ease) forwards; }
    .footer {
        max-width: 1280px; margin: 0 auto; padding: 28px 22px 40px;
        text-align: center; font-size: .76rem; color: var(--text-dim); line-height: 1.6;
    }
    .footer strong { color: var(--text-muted); font-weight: 600; }
    @media print {
        .topbar, .tabs-wrapper, .actions, .transfer-block, .report-actions,
        .footer, .toast-container, .theme-toggle { display: none !important; }
        body {
            background: #fff !important; background-image: none !important;
            padding: 0 !important; color: #000 !important;
        }
        .main { padding: 0 !important; max-width: 100% !important; }
        .panel { display: none !important; }
        .panel.is-active { display: block !important; }
        .panel-grid { grid-template-columns: 1fr !important; gap: 12px !important; }
        .card {
            box-shadow: none !important; border: 1px solid #999 !important;
            page-break-inside: avoid; margin-bottom: 12px !important; background: #fff !important;
        }
        .card + .card { margin-top: 12px !important; }
        .result-card {
            box-shadow: none !important; border: 1px solid #999 !important; background: #fff !important;
        }
        .result-card--primary { background: #f5f5f5 !important; border-color: #666 !important; }
        .result-card--primary .result-card__value,
        .result-card__value { color: #000 !important; }
        .formula-block {
            background: #f9f9f9 !important; border-left: 3px solid #000 !important;
            page-break-inside: avoid;
        }
        .report-document {
            border: none !important; padding: 0 !important; box-shadow: none !important;
            background: #fff !important; color: #000 !important;
        }
        table { border-collapse: collapse !important; }
        .report-doc__table td, .report-doc__table th,
        .report-doc__info-table td {
            border: 1px solid #000 !important; padding: 5px !important;
            background: #fff !important; color: #000 !important;
        }
        .report-doc__table th { background: #e8e8e8 !important; }
        .report-doc__table tr.section-row td { background: #f0f0f0 !important; }
        .report-doc__info-label { background: #f0f0f0 !important; }
        .report-doc__conclusion { border: 1px solid #000 !important; }
        .report-doc__empty { display: none !important; }
        /* Поля ввода при печати выглядят как обычный текст с подчёркиванием */
        .report-doc__input {
            background: transparent !important;
            border: none !important;
            border-bottom: 1px solid #000 !important;
            padding: 0 !important;
            font-weight: 600 !important;
        }
    }
</style>
</head>
<body>

<header class="topbar">
    <div class="topbar__inner">
        <div class="brand">
            <div class="brand__logo">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <path d="M2 20h20"/>
                    <path d="M6 20V8l6-4 6 4v12"/>
                    <path d="M9 20v-5h6v5"/>
                </svg>
            </div>
            <div class="brand__text">
                <div class="brand__title">Инженерный дашборд · ДСУ №1</div>
                <div class="brand__subtitle">Объект: подстанции · Связанные модули</div>
            </div>
        </div>

        <button type="button" class="theme-toggle" id="themeToggle"
                aria-label="Переключить тему" title="Переключить тему">
            <span class="theme-toggle__thumb">
                <svg class="theme-toggle__icon-sun" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="4"/>
                    <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>
                </svg>
                <svg class="theme-toggle__icon-moon" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                </svg>
            </span>
        </button>
    </div>
</header>

<div class="tabs-wrapper">
    <nav class="tabs" role="tablist" aria-label="Модули дашборда">
        <button type="button" class="tab is-active" role="tab"
                aria-selected="true" aria-controls="panel-1" id="tab-1" data-tab="1">
            <span class="tab__icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 12h18"/><path d="M3 6h18"/><path d="M3 18h18"/>
                    <circle cx="8" cy="6" r="1.5" fill="currentColor"/>
                    <circle cx="16" cy="12" r="1.5" fill="currentColor"/>
                    <circle cx="11" cy="18" r="1.5" fill="currentColor"/>
                </svg>
            </span>
            <span class="tab__label">
                <span class="tab__num">Модуль 1</span>
                <span class="tab__name">Доставка асфальтобетона</span>
            </span>
        </button>

        <button type="button" class="tab" role="tab"
                aria-selected="false" aria-controls="panel-2" id="tab-2" data-tab="2">
            <span class="tab__icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <path d="M2 20h20"/><path d="M4 20V10l8-6 8 6v10"/><path d="M9 20v-6h6v6"/>
                </svg>
            </span>
            <span class="tab__label">
                <span class="tab__num">Модуль 2</span>
                <span class="tab__name">Объём земляных работ</span>
            </span>
        </button>

        <button type="button" class="tab" role="tab"
                aria-selected="false" aria-controls="panel-3" id="tab-3" data-tab="3">
            <span class="tab__icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <rect x="1" y="6" width="15" height="12" rx="2"/>
                    <path d="M16 10h4l3 3v5h-7"/>
                    <circle cx="5.5" cy="18.5" r="2"/>
                    <circle cx="18.5" cy="18.5" r="2"/>
                </svg>
            </span>
            <span class="tab__label">
                <span class="tab__num">Модуль 3</span>
                <span class="tab__name">Логистика рейса</span>
            </span>
        </button>

        <button type="button" class="tab" role="tab"
                aria-selected="false" aria-controls="panel-4" id="tab-4" data-tab="4">
            <span class="tab__icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <line x1="16" y1="13" x2="8" y2="13"/>
                    <line x1="16" y1="17" x2="8" y2="17"/>
                </svg>
            </span>
            <span class="tab__label">
                <span class="tab__num">Вкладка 4</span>
                <span class="tab__name">Сводный отчёт</span>
            </span>
        </button>
    </nav>
</div>

<main class="main">

    <section class="panel is-active" id="panel-1" role="tabpanel" aria-labelledby="tab-1">
        <div class="panel-grid">
            <div>
                <div class="card">
                    <div class="card__title">
                        <span class="card__title-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                 stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 20h9"/>
                                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                            </svg>
                        </span>
                        <span class="card__title-text">
                            <span class="card__title-main">Исходные параметры</span>
                            <span class="card__title-sub">Асфальтобетонное покрытие</span>
                        </span>
                    </div>

                    <div class="form-grid">
                        <div class="field field--common">
                            <label class="field__label" for="commonParam-1">
                                Длина участка
                                <span class="field__badge">Общий параметр</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="commonParam-1"
                                       class="field__input common-param"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="1" data-key="L" data-common="true">
                                <span class="field__unit">м</span>
                            </div>
                            <div class="field__hint" id="m1-L-hint">Используется во всех трёх модулях</div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m1-B">
                                Ширина покрытия <span class="field__formula">B</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m1-B" class="field__input"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="1" data-key="B">
                                <span class="field__unit">м</span>
                            </div>
                            <div class="field__hint" id="m1-B-hint"></div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m1-h">
                                Толщина слоя <span class="field__formula">h</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m1-h" class="field__input"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="1" data-key="h">
                                <span class="field__unit">см</span>
                            </div>
                            <div class="field__hint" id="m1-h-hint"></div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m1-rho">
                                Плотность смеси <span class="field__formula">ρ</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m1-rho" class="field__input"
                                       min="0" step="0.01" placeholder="2.4" inputmode="decimal"
                                       data-module="1" data-key="rho" value="2.4">
                                <span class="field__unit">т/м³</span>
                            </div>
                            <div class="field__hint" id="m1-rho-hint">Средняя: 2,3–2,5 т/м³</div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m1-G">
                                Грузоподъёмность <span class="field__formula">G</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m1-G" class="field__input"
                                       min="0" step="any" placeholder="20" inputmode="decimal"
                                       data-module="1" data-key="G" value="20">
                                <span class="field__unit">т</span>
                            </div>
                            <div class="field__hint" id="m1-G-hint">Типовая: 15–30 т</div>
                        </div>
                    </div>

                    <div class="actions">
                        <button type="button" class="btn btn--ghost" data-action="print" data-module="1">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="6 9 6 2 18 2 18 9"/>
                                <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
                                <rect x="6" y="14" width="12" height="8"/>
                            </svg>
                            Печать
                        </button>
                        <button type="button" class="btn btn--secondary" data-action="reset" data-module="1">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="1 4 1 10 7 10"/>
                                <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>
                            </svg>
                            Сброс
                        </button>
                        <button type="button" class="btn btn--primary" data-action="calc" data-module="1">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <rect x="4" y="2" width="16" height="20" rx="2"/>
                                <line x1="8" y1="6" x2="16" y2="6"/>
                                <line x1="8" y1="18" x2="16" y2="18"/>
                            </svg>
                            Рассчитать
                        </button>
                    </div>
                </div>
            </div>

            <div>
                <div class="card">
                    <div class="card__title">
                        <span class="card__title-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.8L7 14"/>
                            </svg>
                        </span>
                        <span class="card__title-text">
                            <span class="card__title-main">Результат расчёта</span>
                            <span class="card__title-sub">Масса смеси и количество рейсов</span>
                        </span>
                    </div>

                    <div class="results-stack">
                        <div class="result-card result-card--primary">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M12 2v20"/><path d="M5 7l7-5 7 5"/><path d="M5 17l7 5 7-5"/>
                                </svg>
                                Площадь покрытия
                            </div>
                            <div class="result-card__value" id="m1-out-area">
                                —<span class="result-card__unit">м²</span>
                            </div>
                            <div class="result-card__sub" id="m1-out-area-sub">S = L × B</div>
                        </div>

                        <div class="result-card result-card--primary">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                                </svg>
                                Масса смеси
                            </div>
                            <div class="result-card__value" id="m1-out-mass">
                                —<span class="result-card__unit">т</span>
                            </div>
                            <div class="result-card__sub" id="m1-out-mass-sub">M = S × (h/100) × ρ</div>
                        </div>

                        <div class="result-card result-card--accent">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <rect x="1" y="6" width="15" height="12" rx="2"/>
                                    <path d="M16 10h4l3 3v5h-7"/>
                                    <circle cx="5.5" cy="18.5" r="2"/>
                                    <circle cx="18.5" cy="18.5" r="2"/>
                                </svg>
                                Количество рейсов
                            </div>
                            <div class="result-card__value" id="m1-out-trips">
                                —<span class="result-card__unit">шт</span>
                            </div>
                            <div class="result-card__sub" id="m1-out-trips-sub">N = ⌈M / G⌉</div>
                        </div>
                    </div>

                    <div class="formula-block">
                        <div class="formula-block__title">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <circle cx="12" cy="12" r="10"/>
                                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                                <line x1="12" y1="17" x2="12.01" y2="17"/>
                            </svg>
                            Формулы расчёта
                        </div>
                        <p>Площадь: <code>S = L × B</code></p>
                        <p>Масса: <code>M = S × (h / 100) × ρ</code></p>
                        <p>Рейсы: <code>N = ⌈M / G⌉</code> (округление вверх)</p>
                    </div>
                </div>

                <div class="transfer-block">
                    <div class="transfer-block__header">
                        <span class="transfer-block__header-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <line x1="5" y1="12" x2="19" y2="12"/>
                                <polyline points="12 5 19 12 12 19"/>
                            </svg>
                        </span>
                        Передача общего параметра
                    </div>
                    <div class="transfer-block__desc">
                        Значение <strong>L — длина участка</strong> будет подставлено
                        в поле общего параметра Модулей 2 и 3.
                    </div>
                    <div class="actions actions--transfer">
                        <button type="button" class="btn btn--warning" id="transferFromM1">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <path d="M4 14l6-6 6 6"/>
                                <path d="M10 8v12"/>
                                <path d="M17 8h3v12h-3"/>
                            </svg>
                            Передать L в Модули 2 и 3
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="panel" id="panel-2" role="tabpanel" aria-labelledby="tab-2">
        <div class="panel-grid">
            <div>
                <div class="card">
                    <div class="card__title">
                        <span class="card__title-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M12 20h9"/>
                                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                            </svg>
                        </span>
                        <span class="card__title-text">
                            <span class="card__title-main">Исходные параметры</span>
                            <span class="card__title-sub">Геометрия выемки / насыпи</span>
                        </span>
                    </div>

                    <div class="form-grid">
                        <div class="field field--common">
                            <label class="field__label" for="commonParam-2">
                                Длина участка
                                <span class="field__badge">Общий параметр</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="commonParam-2"
                                       class="field__input common-param"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="2" data-key="L" data-common="true">
                                <span class="field__unit">м</span>
                            </div>
                            <div class="field__hint" id="m2-L-hint">Можно получить из Модуля 1</div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m2-B">
                                Ширина выемки <span class="field__formula">B</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m2-B" class="field__input"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="2" data-key="B">
                                <span class="field__unit">м</span>
                            </div>
                            <div class="field__hint" id="m2-B-hint"></div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m2-H">
                                Глубина / высота <span class="field__formula">H</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m2-H" class="field__input"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="2" data-key="H">
                                <span class="field__unit">м</span>
                            </div>
                            <div class="field__hint" id="m2-H-hint"></div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m2-rho">
                                Плотность грунта <span class="field__formula">ρ</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m2-rho" class="field__input"
                                       min="0" step="0.01" placeholder="1.8" inputmode="decimal"
                                       data-module="2" data-key="rho" value="1.8">
                                <span class="field__unit">т/м³</span>
                            </div>
                            <div class="field__hint" id="m2-rho-hint">Средняя: 1,6–2,0 т/м³</div>
                        </div>
                    </div>

                    <div class="actions">
                        <button type="button" class="btn btn--ghost" data-action="print" data-module="2">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="6 9 6 2 18 2 18 9"/>
                                <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
                                <rect x="6" y="14" width="12" height="8"/>
                            </svg>
                            Печать
                        </button>
                        <button type="button" class="btn btn--secondary" data-action="reset" data-module="2">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="1 4 1 10 7 10"/>
                                <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>
                            </svg>
                            Сброс
                        </button>
                        <button type="button" class="btn btn--primary" data-action="calc" data-module="2">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <rect x="4" y="2" width="16" height="20" rx="2"/>
                                <line x1="8" y1="6" x2="16" y2="6"/>
                                <line x1="8" y1="18" x2="16" y2="18"/>
                            </svg>
                            Рассчитать
                        </button>
                    </div>
                </div>
            </div>

            <div>
                <div class="card">
                    <div class="card__title">
                        <span class="card__title-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.8L7 14"/>
                            </svg>
                        </span>
                        <span class="card__title-text">
                            <span class="card__title-main">Результат расчёта</span>
                            <span class="card__title-sub">Объём и масса грунта</span>
                        </span>
                    </div>

                    <div class="results-stack">
                        <div class="result-card result-card--primary">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                                </svg>
                                Объём выемки
                            </div>
                            <div class="result-card__value" id="m2-out-volume">
                                —<span class="result-card__unit">м³</span>
                            </div>
                            <div class="result-card__sub" id="m2-out-volume-sub">V = L × B × H</div>
                        </div>

                        <div class="result-card result-card--accent">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M12 2v20"/><path d="M5 7l7-5 7 5"/><path d="M5 17l7 5 7-5"/>
                                </svg>
                                Масса грунта
                            </div>
                            <div class="result-card__value" id="m2-out-mass">
                                —<span class="result-card__unit">т</span>
                            </div>
                            <div class="result-card__sub" id="m2-out-mass-sub">M = V × ρ</div>
                        </div>
                    </div>

                    <div class="formula-block">
                        <div class="formula-block__title">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <circle cx="12" cy="12" r="10"/>
                                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                                <line x1="12" y1="17" x2="12.01" y2="17"/>
                            </svg>
                            Формулы расчёта
                        </div>
                        <p>Объём: <code>V = L × B × H</code></p>
                        <p>Масса: <code>M = V × ρ</code></p>
                    </div>
                </div>

                <div class="transfer-block">
                    <div class="transfer-block__header">
                        <span class="transfer-block__header-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <line x1="5" y1="12" x2="19" y2="12"/>
                                <polyline points="12 5 19 12 12 19"/>
                            </svg>
                        </span>
                        Передача общего параметра
                    </div>
                    <div class="transfer-block__desc">
                        Если значение <strong>L</strong> в этом модуле было изменено,
                        его можно передать в Модуль 3.
                    </div>
                    <div class="actions actions--transfer">
                        <button type="button" class="btn btn--warning" id="transferFromM2">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <path d="M4 14l6-6 6 6"/>
                                <path d="M10 8v12"/>
                                <path d="M17 8h3v12h-3"/>
                            </svg>
                            Передать L в Модуль 3
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="panel" id="panel-3" role="tabpanel" aria-labelledby="tab-3">
        <div class="panel-grid">
            <div>
                <div class="card">
                    <div class="card__title">
                        <span class="card__title-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M12 20h9"/>
                                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                            </svg>
                        </span>
                        <span class="card__title-text">
                            <span class="card__title-main">Исходные параметры</span>
                            <span class="card__title-sub">Параметры транспортного цикла</span>
                        </span>
                    </div>

                    <div class="form-grid">
                        <div class="field field--common">
                            <label class="field__label" for="commonParam-3">
                                Расстояние рейса
                                <span class="field__badge">Общий параметр</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="commonParam-3"
                                       class="field__input common-param"
                                       min="0" step="any" placeholder="0" inputmode="decimal"
                                       data-module="3" data-key="L" data-common="true">
                                <span class="field__unit">м</span>
                            </div>
                            <div class="field__hint" id="m3-L-hint">В метрах; пересчёт в км автоматический</div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m3-V">
                                Средняя скорость <span class="field__formula">V</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m3-V" class="field__input"
                                       min="0" step="any" placeholder="40" inputmode="decimal"
                                       data-module="3" data-key="V" value="40">
                                <span class="field__unit">км/ч</span>
                            </div>
                            <div class="field__hint" id="m3-V-hint">Типовая: 30–60 км/ч</div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m3-tLoad">
                                Время погрузки <span class="field__formula">t п</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m3-tLoad" class="field__input"
                                       min="0" step="any" placeholder="10" inputmode="decimal"
                                       data-module="3" data-key="tLoad" value="10">
                                <span class="field__unit">мин</span>
                            </div>
                            <div class="field__hint" id="m3-tLoad-hint"></div>
                        </div>

                        <div class="field">
                            <label class="field__label" for="m3-tUnload">
                                Время разгрузки <span class="field__formula">t р</span>
                            </label>
                            <div class="field__wrap">
                                <input type="number" id="m3-tUnload" class="field__input"
                                       min="0" step="any" placeholder="8" inputmode="decimal"
                                       data-module="3" data-key="tUnload" value="8">
                                <span class="field__unit">мин</span>
                            </div>
                            <div class="field__hint" id="m3-tUnload-hint"></div>
                        </div>
                    </div>

                    <div class="actions">
                        <button type="button" class="btn btn--ghost" data-action="print" data-module="3">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="6 9 6 2 18 2 18 9"/>
                                <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
                                <rect x="6" y="14" width="12" height="8"/>
                            </svg>
                            Печать
                        </button>
                        <button type="button" class="btn btn--secondary" data-action="reset" data-module="3">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="1 4 1 10 7 10"/>
                                <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>
                            </svg>
                            Сброс
                        </button>
                        <button type="button" class="btn btn--primary" data-action="calc" data-module="3">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <rect x="4" y="2" width="16" height="20" rx="2"/>
                                <line x1="8" y1="6" x2="16" y2="6"/>
                                <line x1="8" y1="18" x2="16" y2="18"/>
                            </svg>
                            Рассчитать
                        </button>
                    </div>
                </div>
            </div>

            <div>
                <div class="card">
                    <div class="card__title">
                        <span class="card__title-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.8L7 14"/>
                            </svg>
                        </span>
                        <span class="card__title-text">
                            <span class="card__title-main">Результат расчёта</span>
                            <span class="card__title-sub">Длительность рейса</span>
                        </span>
                    </div>

                    <div class="results-stack">
                        <div class="result-card result-card--primary">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <circle cx="12" cy="12" r="10"/>
                                    <polyline points="12 6 12 12 16 14"/>
                                </svg>
                                Полное время рейса
                            </div>
                            <div class="result-card__value" id="m3-out-time">
                                —<span class="result-card__unit">мин</span>
                            </div>
                            <div class="result-card__sub" id="m3-out-time-sub">T = (2L / V) × 60 + t п + t р</div>
                        </div>

                        <div class="result-card result-card--accent">
                            <div class="result-card__label">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M12 2v20"/><path d="M5 7l7-5 7 5"/><path d="M5 17l7 5 7-5"/>
                                </svg>
                                Рейсов за смену (8 ч)
                            </div>
                            <div class="result-card__value" id="m3-out-shift">
                                —<span class="result-card__unit">шт</span>
                            </div>
                            <div class="result-card__sub" id="m3-out-shift-sub">n = ⌊480 / T⌋</div>
                        </div>
                    </div>

                    <div class="formula-block">
                        <div class="formula-block__title">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <circle cx="12" cy="12" r="10"/>
                                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                                <line x1="12" y1="17" x2="12.01" y2="17"/>
                            </svg>
                            Формулы расчёта
                        </div>
                        <p>Время рейса: <code>T = (2L / V) × 60 + t п + t р</code>,
                            где <em>L</em> — расстояние (км),
                            <em>V</em> — скорость (км/ч),
                            <em>t п</em> — время погрузки (мин),
                            <em>t р</em> — время разгрузки (мин).</p>
                        <p>Рейсов за смену: <code>n = ⌊480 / T⌋</code></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="panel" id="panel-4" role="tabpanel" aria-labelledby="tab-4">
        <div class="card">
            <div class="card__title">
                <span class="card__title-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                    </svg>
                </span>
                <span class="card__title-text">
                    <span class="card__title-main">Сводный отчёт по проекту</span>
                    <span class="card__title-sub">Технический отчёт по результатам инженерных расчётов</span>
                </span>
            </div>

            <div class="report-actions">
                <button type="button" class="btn btn--primary" id="generateReport">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.8L7 14"/>
                    </svg>
                    Сформировать отчёт
                </button>
                <button type="button" class="btn btn--word" id="downloadWord">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/>
                        <line x1="12" y1="15" x2="12" y2="3"/>
                    </svg>
                    Скачать отчёт в Word
                </button>
                <button type="button" class="btn btn--success" id="saveProject">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/>
                        <polyline points="17 21 17 13 7 13 7 21"/>
                        <polyline points="7 3 7 8 15 8"/>
                    </svg>
                    Сохранить проект
                </button>
                <button type="button" class="btn btn--ghost" id="printReport">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="6 9 6 2 18 2 18 9"/>
                        <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
                        <rect x="6" y="14" width="12" height="8"/>
                    </svg>
                    Печать / Сохранить в PDF
                </button>
            </div>

            <div class="report-document" id="reportDocument">
                <div class="report-doc__empty">
                    Заполните данные в Модулях 1–3, чтобы сформировать технический отчёт.
                </div>
            </div>
        </div>
    </section>

</main>

<footer class="footer">
    <strong>ООО «Дорожно-Строительное Управление №1»</strong> · Объект: подстанции · Шифр: 7715800287<br>
    Формулы соответствуют СП 78.13330.2012, СП 34.13330.2021, ГОСТ 9128-2013
</footer>

<div class="toast-container" id="toastContainer" aria-live="polite" aria-atomic="true"></div>

<script>
(function () {
    'use strict';

    /* =================================================================
       КОНСТАНТЫ И СОСТОЯНИЕ
       ================================================================= */
    var STORAGE_KEY = 'dsu1-dashboard-project-v2';
    var THEME_KEY   = 'dsu1-dashboard-theme';

    var REPORT_META_DEFAULTS = {
        org:    'ООО «Дорожно-Строительное Управление №1»',
        object: 'подстанции',
        code:   '7715800287'
    };

    var DEFAULT_VALUES = {
        1: { L: '', B: '', h: '', rho: '2.4', G: '20' },
        2: { L: '', B: '', H: '', rho: '1.8' },
        3: { L: '', V: '40', tLoad: '10', tUnload: '8' }
    };

    var state = {
        activeTab: '1',
        theme: 'light',
        reportMeta: Object.assign({}, REPORT_META_DEFAULTS),
        modules: {
            1: { values: Object.assign({}, DEFAULT_VALUES[1]), result: null },
            2: { values: Object.assign({}, DEFAULT_VALUES[2]), result: null },
            3: { values: Object.assign({}, DEFAULT_VALUES[3]), result: null }
        }
    };

    var RULES = {
        1: {
            L:    { min: 0.01, max: 1e6, label: 'Длина участка' },
            B:    { min: 0.01, max: 1e4, label: 'Ширина покрытия' },
            h:    { min: 0.1,  max: 100, label: 'Толщина слоя' },
            rho:  { min: 0.5,  max: 5,   label: 'Плотность смеси' },
            G:    { min: 0.1,  max: 200, label: 'Грузоподъёмность' }
        },
        2: {
            L:    { min: 0.01, max: 1e6, label: 'Длина участка' },
            B:    { min: 0.01, max: 1e4, label: 'Ширина выемки' },
            H:    { min: 0.01, max: 100, label: 'Глубина' },
            rho:  { min: 0.5,  max: 5,   label: 'Плотность грунта' }
        },
        3: {
            L:       { min: 1, max: 1e6, label: 'Расстояние' },
            V:       { min: 1, max: 150, label: 'Скорость' },
            tLoad:   { min: 0, max: 600, label: 'Время погрузки' },
            tUnload: { min: 0, max: 600, label: 'Время разгрузки' }
        }
    };

    /* =================================================================
       УТИЛИТЫ
       ================================================================= */
    function $(sel, ctx) { return (ctx || document).querySelector(sel); }
    function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

    function parseNum(value) {
        if (value === null || value === undefined) return NaN;
        var s = String(value).trim().replace(',', '.');
        if (s === '') return NaN;
        var n = Number(s);
        return Number.isFinite(n) ? n : NaN;
    }

    function fmt(num, digits) {
        if (!Number.isFinite(num)) return '—';
        return num.toLocaleString('ru-RU', {
            minimumFractionDigits: 0,
            maximumFractionDigits: typeof digits === 'number' ? digits : 2
        });
    }

    function escapeHtml(str) {
        return String(str).replace(/[&<>"']/g, function (c) {
            return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
        });
    }

    /* =================================================================
       TOAST-УВЕДОМЛЕНИЯ
       ================================================================= */
    function showToast(message, type) {
        var container = $('#toastContainer');
        if (!container) return;

        var icons = {
            success: '<polyline points="20 6 9 17 4 12"/>',
            error:   '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>',
            info:    '<circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>'
        };

        var toast = document.createElement('div');
        toast.className = 'toast toast--' + (type || 'info');
        toast.innerHTML =
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
            'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' +
            (icons[type] || icons.info) + '</svg>' +
            '<div>' + escapeHtml(message) + '</div>';
        container.appendChild(toast);

        setTimeout(function () {
            toast.classList.add('is-leaving');
            setTimeout(function () { toast.remove(); }, 320);
        }, 3200);
    }

    /* =================================================================
       ВАЛИДАЦИЯ
       ================================================================= */
    function validateField(moduleId, key) {
        var rule = RULES[moduleId][key];
        var raw = state.modules[moduleId].values[key];
        var value = parseNum(raw);

        if (raw === '' || raw === null || raw === undefined) {
            return { valid: false, empty: true, value: NaN, message: '' };
        }
        if (!Number.isFinite(value)) {
            return { valid: false, empty: false, value: NaN, message: 'Введите число' };
        }
        if (value < 0) {
            return { valid: false, empty: false, value: value, message: 'Отрицательные значения запрещены' };
        }
        if (value < rule.min) {
            return { valid: false, empty: false, value: value, message: 'Минимум: ' + fmt(rule.min, 4) };
        }
        if (value > rule.max) {
            return { valid: false, empty: false, value: value, message: 'Максимум: ' + fmt(rule.max, 4) };
        }
        return { valid: true, empty: false, value: value, message: '' };
    }

    function updateFieldUI(moduleId, key, validation) {
        var input = $('[data-module="' + moduleId + '"][data-key="' + key + '"]');
        var hint  = $('#m' + moduleId + '-' + key + '-hint');
        if (!input) return;

        var defaultHints = {
            '1-L':   'Используется во всех трёх модулях',
            '1-rho': 'Средняя: 2,3–2,5 т/м³',
            '1-G':   'Типовая: 15–30 т',
            '2-L':   'Можно получить из Модуля 1',
            '2-rho': 'Средняя: 1,6–2,0 т/м³',
            '3-L':   'В метрах; пересчёт в км автоматический',
            '3-V':   'Типовая: 30–60 км/ч'
        };
        var hintKey = moduleId + '-' + key;

        if (validation.empty) {
            input.classList.remove('is-invalid');
            if (hint) {
                hint.textContent = defaultHints[hintKey] || '';
                hint.classList.remove('is-error');
            }
            return;
        }

        if (!validation.valid) {
            input.classList.add('is-invalid');
            if (hint) {
                hint.textContent = validation.message;
                hint.classList.add('is-error');
            }
        } else {
            input.classList.remove('is-invalid');
            if (hint) {
                hint.textContent = defaultHints[hintKey] || '';
                hint.classList.remove('is-error');
            }
        }
    }

    /* =================================================================
       ФОРМУЛЫ МОДУЛЕЙ
       ================================================================= */
    function calcModule1(v) {
        var S = v.L * v.B;
        var mass = S * (v.h / 100) * v.rho;
        var trips = Math.ceil(mass / v.G);
        return {
            S: S, mass: mass, trips: trips,
            lastLoad: trips > 0 ? mass - (trips - 1) * v.G : 0,
            L: v.L, B: v.B, h: v.h, rho: v.rho, G: v.G
        };
    }

    function calcModule2(v) {
        var volume = v.L * v.B * v.H;
        var mass = volume * v.rho;
        return { volume: volume, mass: mass, L: v.L, B: v.B, H: v.H, rho: v.rho };
    }

    function calcModule3(v) {
        var distanceKm = v.L / 1000;
        var travelMin = (2 * distanceKm / v.V) * 60;
        var total = travelMin + v.tLoad + v.tUnload;
        var shifts = total > 0 ? Math.floor(480 / total) : 0;
        return {
            total: total, travelMin: travelMin, distanceKm: distanceKm, shifts: shifts,
            L: v.L, V: v.V, tLoad: v.tLoad, tUnload: v.tUnload
        };
    }

    /* =================================================================
       РЕНДЕР РЕЗУЛЬТАТОВ
       ================================================================= */
    function renderResultEmpty(moduleId) {
        if (moduleId === 1) {
            $('#m1-out-area').innerHTML  = '—<span class="result-card__unit">м²</span>';
            $('#m1-out-area-sub').textContent = 'S = L × B';
            $('#m1-out-mass').innerHTML  = '—<span class="result-card__unit">т</span>';
            $('#m1-out-mass-sub').textContent = 'M = S × (h/100) × ρ';
            $('#m1-out-trips').innerHTML = '—<span class="result-card__unit">шт</span>';
            $('#m1-out-trips-sub').textContent = 'N = ⌈M / G⌉';
        } else if (moduleId === 2) {
            $('#m2-out-volume').innerHTML = '—<span class="result-card__unit">м³</span>';
            $('#m2-out-volume-sub').textContent = 'V = L × B × H';
            $('#m2-out-mass').innerHTML   = '—<span class="result-card__unit">т</span>';
            $('#m2-out-mass-sub').textContent = 'M = V × ρ';
        } else if (moduleId === 3) {
            $('#m3-out-time').innerHTML  = '—<span class="result-card__unit">мин</span>';
            $('#m3-out-time-sub').textContent = 'T = (2L / V) × 60 + t п + t р';
            $('#m3-out-shift').innerHTML = '—<span class="result-card__unit">шт</span>';
            $('#m3-out-shift-sub').textContent = 'n = ⌊480 / T⌋';
        }
    }

    function renderResultError(moduleId) {
        var errText = 'исправьте ошибки в полях ввода';
        if (moduleId === 1) {
            $('#m1-out-area').innerHTML  = '—<span class="result-card__unit">м²</span>';
            $('#m1-out-area-sub').textContent = errText;
            $('#m1-out-mass').innerHTML  = '—<span class="result-card__unit">т</span>';
            $('#m1-out-mass-sub').textContent = errText;
            $('#m1-out-trips').innerHTML = '—<span class="result-card__unit">шт</span>';
            $('#m1-out-trips-sub').textContent = errText;
        } else if (moduleId === 2) {
            $('#m2-out-volume').innerHTML = '—<span class="result-card__unit">м³</span>';
            $('#m2-out-volume-sub').textContent = errText;
            $('#m2-out-mass').innerHTML   = '—<span class="result-card__unit">т</span>';
            $('#m2-out-mass-sub').textContent = errText;
        } else if (moduleId === 3) {
            $('#m3-out-time').innerHTML  = '—<span class="result-card__unit">мин</span>';
            $('#m3-out-time-sub').textContent = errText;
            $('#m3-out-shift').innerHTML = '—<span class="result-card__unit">шт</span>';
            $('#m3-out-shift-sub').textContent = errText;
        }
    }

    function renderResult(moduleId) {
        var result = state.modules[moduleId].result;
        if (!result) { renderResultEmpty(moduleId); return; }

        if (moduleId === 1) {
            $('#m1-out-area').innerHTML = fmt(result.S, 2) + '<span class="result-card__unit">м²</span>';
            $('#m1-out-area-sub').textContent = 'S = ' + fmt(result.L, 1) + ' × ' + fmt(result.B, 1);
            $('#m1-out-mass').innerHTML = fmt(result.mass, 2) + '<span class="result-card__unit">т</span>';
            $('#m1-out-mass-sub').textContent = 'при ρ = ' + fmt(result.rho, 2) + ' т/м³ и h = ' + fmt(result.h, 1) + ' см';
            $('#m1-out-trips').innerHTML = fmt(result.trips, 0) + '<span class="result-card__unit">шт</span>';
            if (result.trips > 0) {
                $('#m1-out-trips-sub').textContent = 'загрузка последнего рейса: ' + fmt(result.lastLoad, 2) + ' т';
            } else {
                $('#m1-out-trips-sub').textContent = '—';
            }
        } else if (moduleId === 2) {
            $('#m2-out-volume').innerHTML = fmt(result.volume, 2) + '<span class="result-card__unit">м³</span>';
            $('#m2-out-volume-sub').textContent = 'V = ' + fmt(result.L, 1) + ' × ' + fmt(result.B, 1) + ' × ' + fmt(result.H, 2);
            $('#m2-out-mass').innerHTML = fmt(result.mass, 2) + '<span class="result-card__unit">т</span>';
            $('#m2-out-mass-sub').textContent = 'при ρ = ' + fmt(result.rho, 2) + ' т/м³';
        } else if (moduleId === 3) {
            $('#m3-out-time').innerHTML = fmt(result.total, 1) + '<span class="result-card__unit">мин</span>';
            $('#m3-out-time-sub').textContent =
                'в пути: ' + fmt(result.travelMin, 1) + ' мин (' +
                fmt(result.distanceKm, 2) + ' км в одну сторону) · ' +
                'погрузка: ' + fmt(result.tLoad, 1) + ' · ' +
                'разгрузка: ' + fmt(result.tUnload, 1);
            $('#m3-out-shift').innerHTML = fmt(result.shifts, 0) + '<span class="result-card__unit">шт</span>';
            $('#m3-out-shift-sub').textContent = 'за 8-часовую смену (480 мин)';
        }
    }

    /* =================================================================
       РАСЧЁТ МОДУЛЯ
       ================================================================= */
    function calculateModule(moduleId) {
        var values = state.modules[moduleId].values;
        var keys = Object.keys(RULES[moduleId]);

        var allValid = true;
        var filled = 0;

        for (var i = 0; i < keys.length; i++) {
            var key = keys[i];
            var v = validateField(moduleId, key);
            updateFieldUI(moduleId, key, v);
            if (v.empty) allValid = false;
            else if (!v.valid) allValid = false;
            else filled++;
        }

        if (filled < keys.length) {
            state.modules[moduleId].result = null;
            renderResultEmpty(moduleId);
            return;
        }
        if (!allValid) {
            state.modules[moduleId].result = null;
            renderResultError(moduleId);
            return;
        }

        var numeric = {};
        for (var j = 0; j < keys.length; j++) {
            numeric[keys[j]] = parseNum(values[keys[j]]);
        }

        var result;
        if (moduleId === 1)      result = calcModule1(numeric);
        else if (moduleId === 2) result = calcModule2(numeric);
        else                     result = calcModule3(numeric);

        state.modules[moduleId].result = result;
        renderResult(moduleId);
    }

    /* =================================================================
       ПЕРЕДАЧА ОБЩЕГО ПАРАМЕТРА
       ================================================================= */
    function transferCommonParam(fromModuleId, toModuleIds) {
        var sourceValue = state.modules[fromModuleId].values.L;
        var parsed = parseNum(sourceValue);

        if (!Number.isFinite(parsed) || parsed <= 0) {
            showToast('Введите корректное положительное значение L в Модуле ' + fromModuleId, 'error');
            return;
        }

        toModuleIds.forEach(function (mid) {
            state.modules[mid].values.L = sourceValue;
            var input = $('[data-module="' + mid + '"][data-key="L"]');
            if (input) input.value = sourceValue;
            calculateModule(mid);
        });

        var moduleNames = toModuleIds.join(' и ');
        showToast(
            'L = ' + fmt(parsed, 2) + ' м передано в Модул' +
            (toModuleIds.length > 1 ? 'и ' : 'ь ') + moduleNames,
            'success'
        );

        switchTab(String(toModuleIds[0]));
    }

    /* =================================================================
       ВКЛАДКИ
       ================================================================= */
    function switchTab(tabId) {
        state.activeTab = String(tabId);

        $$('.tab').forEach(function (t) {
            var isActive = t.dataset.tab === String(tabId);
            t.classList.toggle('is-active', isActive);
            t.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });

        $$('.panel').forEach(function (p) {
            p.classList.toggle('is-active', p.id === 'panel-' + tabId);
        });

        var numericTab = Number(tabId);
        if (numericTab >= 1 && numericTab <= 3) {
            calculateModule(numericTab);
        } else if (numericTab === 4) {
            renderReportDocument();
        }
    }

    /* =================================================================
       ТЕМА
       ================================================================= */
    function applyTheme(theme) {
        state.theme = theme;
        document.documentElement.setAttribute('data-theme', theme);
        try { localStorage.setItem(THEME_KEY, theme); } catch (e) {}
    }

    function initTheme() {
        var saved = null;
        try { saved = localStorage.getItem(THEME_KEY); } catch (e) {}
        if (saved === 'dark' || saved === 'light') {
            applyTheme(saved);
        } else {
            var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            applyTheme(prefersDark ? 'dark' : 'light');
        }
    }

    /* =================================================================
       СБРОС МОДУЛЯ
       ================================================================= */
    function resetModule(moduleId) {
        var defaults = DEFAULT_VALUES[moduleId];
        state.modules[moduleId].values = Object.assign({}, defaults);
        state.modules[moduleId].result = null;

        Object.keys(defaults).forEach(function (key) {
            var input = $('[data-module="' + moduleId + '"][data-key="' + key + '"]');
            if (input) input.value = defaults[key];
        });

        $$('[data-module="' + moduleId + '"]').forEach(function (el) {
            el.classList.remove('is-invalid');
        });
        $$('[id^="m' + moduleId + '-"][id$="-hint"]').forEach(function (el) {
            el.classList.remove('is-error');
        });

        var baseHints = {
            '1-L':   'Используется во всех трёх модулях',
            '1-rho': 'Средняя: 2,3–2,5 т/м³',
            '1-G':   'Типовая: 15–30 т',
            '2-L':   'Можно получить из Модуля 1',
            '2-rho': 'Средняя: 1,6–2,0 т/м³',
            '3-L':   'В метрах; пересчёт в км автоматический',
            '3-V':   'Типовая: 30–60 км/ч'
        };
        Object.keys(baseHints).forEach(function (id) {
            var el = $('#m' + id + '-hint');
            if (el) el.textContent = baseHints[id];
        });

        renderResultEmpty(moduleId);
        renderReportDocument();
        showToast('Модуль ' + moduleId + ' сброшен', 'info');
    }

    /* =================================================================
       ФОРМИРОВАНИЕ HTML ОТЧЁТА
       ================================================================= */
    function buildReportHTML() {
        var m1 = state.modules[1].result;
        var m2 = state.modules[2].result;
        var m3 = state.modules[3].result;
        var v1 = state.modules[1].values;
        var v2 = state.modules[2].values;
        var v3 = state.modules[3].values;
        var meta = state.reportMeta;

        var hasAny = m1 || m2 || m3;
        if (!hasAny) {
            return '<div class="report-doc__empty">' +
                   'Заполните данные в Модулях 1–3, чтобы сформировать технический отчёт.' +
                   '</div>';
        }

        var dateStr = new Date().toLocaleDateString('ru-RU');

        function val(v, digits) {
            return Number.isFinite(v) ? fmt(v, digits) : '—';
        }

        function row(name, symb, value, unit) {
            return '<tr>' +
                '<td>' + escapeHtml(name) + '</td>' +
                '<td>' + escapeHtml(symb) + '</td>' +
                '<td class="num">' + value + '</td>' +
                '<td>' + escapeHtml(unit) + '</td>' +
            '</tr>';
        }

        function sectionRow(title) {
            return '<tr class="section-row"><td colspan="4">' + escapeHtml(title) + '</td></tr>';
        }

        /* -------- Блок 1. Общие сведения -------- */
        var generalBlock = '' +
            '<div class="report-doc__section">' +
                '<h2 class="report-doc__section-title">1. Общие сведения</h2>' +
                '<table class="report-doc__info-table">' +
                    '<tr>' +
                        '<td class="report-doc__info-label">Организация</td>' +
                        '<td>' +
                            '<input type="text" ' +
                            'class="report-doc__input" ' +
                            'data-report-key="org" ' +
                            'value="' + escapeHtml(meta.org) + '" ' +
                            'placeholder="Название организации" ' +
                            'aria-label="Название организации">' +
                        '</td>' +
                    '</tr>' +
                    '<tr>' +
                        '<td class="report-doc__info-label">Наименование объекта</td>' +
                        '<td>' +
                            '<input type="text" ' +
                            'class="report-doc__input" ' +
                            'data-report-key="object" ' +
                            'value="' + escapeHtml(meta.object) + '" ' +
                            'placeholder="Наименование объекта" ' +
                            'aria-label="Наименование объекта">' +
                        '</td>' +
                    '</tr>' +
                    '<tr>' +
                        '<td class="report-doc__info-label">Шифр проекта</td>' +
                        '<td>' +
                            '<input type="text" ' +
                            'class="report-doc__input" ' +
                            'data-report-key="code" ' +
                            'value="' + escapeHtml(meta.code) + '" ' +
                            'placeholder="Шифр проекта" ' +
                            'aria-label="Шифр проекта">' +
                        '</td>' +
                    '</tr>' +
                '</table>' +
            '</div>';

        /* -------- Результаты инженерных расчётов -------- */
        var rows = '';

        rows += sectionRow('Модуль 1. Калькулятор доставки асфальтобетона');
        rows += row('Длина участка', 'L', val(parseNum(v1.L), 2), 'м');
        rows += row('Ширина покрытия', 'B', val(parseNum(v1.B), 2), 'м');
        rows += row('Толщина слоя', 'h', val(parseNum(v1.h), 1), 'см');
        rows += row('Плотность смеси', 'ρ', val(parseNum(v1.rho), 2), 'т/м³');
        rows += row('Грузоподъёмность самосвала', 'G', val(parseNum(v1.G), 2), 'т');
        rows += row('Площадь покрытия', 'S = L × B', val(m1 ? m1.S : NaN, 2), 'м²');
        rows += row('Масса асфальтобетонной смеси', 'M = S × (h/100) × ρ', val(m1 ? m1.mass : NaN, 2), 'т');
        rows += row('Количество рейсов', 'N = ⌈M / G⌉', m1 ? fmt(m1.trips, 0) : '—', 'шт');

        rows += sectionRow('Модуль 2. Объём земляных работ');
        rows += row('Длина участка', 'L', val(parseNum(v2.L), 2), 'м');
        rows += row('Ширина выемки', 'B', val(parseNum(v2.B), 2), 'м');
        rows += row('Глубина / высота', 'H', val(parseNum(v2.H), 2), 'м');
        rows += row('Плотность грунта', 'ρ', val(parseNum(v2.rho), 2), 'т/м³');
        rows += row('Объём выемки', 'V = L × B × H', val(m2 ? m2.volume : NaN, 2), 'м³');
        rows += row('Масса грунта', 'M = V × ρ', val(m2 ? m2.mass : NaN, 2), 'т');

        rows += sectionRow('Модуль 3. Логистика рейса');
        rows += row('Расстояние в одну сторону', 'L', val(parseNum(v3.L), 2), 'м');
        rows += row('Средняя скорость', 'V', val(parseNum(v3.V), 1), 'км/ч');
        rows += row('Время погрузки', 't п', val(parseNum(v3.tLoad), 1), 'мин');
        rows += row('Время разгрузки', 't р', val(parseNum(v3.tUnload), 1), 'мин');
        rows += row('Полное время рейса', 'T = (2L / V) × 60 + t п + t р', val(m3 ? m3.total : NaN, 1), 'мин');
        rows += row('Рейсов за смену 8 ч', 'n = ⌊480 / T⌋', m3 ? fmt(m3.shifts, 0) : '—', 'шт');

        var resultsBlock = '' +
            '<div class="report-doc__section">' +
                '<h2 class="report-doc__section-title">Результаты инженерных расчётов</h2>' +
                '<table class="report-doc__table">' +
                    '<thead>' +
                        '<tr>' +
                            '<th>Наименование параметра</th>' +
                            '<th>Обозначение / формула</th>' +
                            '<th>Значение</th>' +
                            '<th>Ед. изм.</th>' +
                        '</tr>' +
                    '</thead>' +
                    '<tbody>' + rows + '</tbody>' +
                '</table>' +
            '</div>';

        /* -------- Блок 2. Заключение инженера ПТО (статический текст) -------- */
        var conclusionBlock = '' +
            '<div class="report-doc__section">' +
                '<h2 class="report-doc__section-title">2. Заключение инженера ПТО</h2>' +
                '<div class="report-doc__conclusion">' +
                    '<p>Параметры объекта соответствуют нормативным требованиям. ' +
                    'Объект допущен к производству строительно-монтажных работ.</p>' +
                '</div>' +
            '</div>';

        /* -------- Шапка (letterhead) -------- */
        var headerHtml = '' +
            '<div class="report-doc__header">' +
                '<div class="report-doc__org">' +
                    escapeHtml(meta.org || 'Организация не указана') +
                '</div>' +
            '</div>';

        /* -------- Сборка -------- */
        return '' +
            headerHtml +
            '<h1 class="report-doc__title">' +
                'ТЕХНИЧЕСКИЙ ОТЧЁТ ПО РЕЗУЛЬТАТАМ ИНЖЕНЕРНЫХ РАСЧЁТОВ' +
            '</h1>' +
            '<div class="report-doc__date">Дата формирования: ' + dateStr + '</div>' +
            generalBlock +
            resultsBlock +
            conclusionBlock +
            '<div class="report-doc__signature">' +
                'Инженер ПТО&nbsp;' +
                '<span class="report-doc__signature-line"></span>' +
                ' / ' +
                '<span class="report-doc__signature-line"></span>' +
                ' /' +
                '<div class="report-doc__mp">М.П.</div>' +
            '</div>';
    }

    function renderReportDocument() {
        var container = $('#reportDocument');
        if (!container) return;
        container.innerHTML = buildReportHTML();
    }

    function generateReport() {
        var m1 = state.modules[1].result;
        var m2 = state.modules[2].result;
        var m3 = state.modules[3].result;

        if (!m1 && !m2 && !m3) {
            showToast('Нет данных для отчёта — заполните хотя бы один модуль', 'error');
            return;
        }

        renderReportDocument();
        showToast('Отчёт сформирован', 'success');
    }

    /* =================================================================
       ОБРАБОТЧИК ВВОДА В ПОЛЯ ОБЩИХ СВЕДЕНИЙ
       -----------------------------------------------------------------
       Делегирование события input на #reportDocument — работает даже
       после многократных перерисовок внутренностей контейнера.
       При вводе: обновляем state.reportMeta и синхронизируем шапку.
       ================================================================= */
    function handleReportMetaInput(e) {
        var key = e.target.dataset.reportKey;
        if (!key) return;
        if (!(key in state.reportMeta)) return;

        state.reportMeta[key] = e.target.value;

        // Синхронизация шапки (letterhead) в реальном времени
        if (key === 'org') {
            var orgEl = document.querySelector('#reportDocument .report-doc__org');
            if (orgEl) {
                orgEl.textContent = e.target.value || 'Организация не указана';
            }
        }
    }

    /* =================================================================
       ЭКСПОРТ ОТЧЁТА В WORD (исправленная надёжная версия)
       -----------------------------------------------------------------
       Новое:
         • Перед чтением innerHTML клонируем содержимое и заменяем
           <input class="report-doc__input"> на <span> с их значениями.
           Это гарантирует, что текстовые поля «1. Общие сведения»
           попадут в Word как обычный текст, а не как form fields.
       ================================================================= */
    function downloadWord() {
        try {
            var m1 = state.modules[1].result;
            var m2 = state.modules[2].result;
            var m3 = state.modules[3].result;

            if (!m1 && !m2 && !m3) {
                showToast('Нет данных для экспорта — заполните модули', 'error');
                return;
            }

            // Актуализируем содержимое отчёта
            renderReportDocument();

            var content = document.getElementById('reportDocument');
            if (!content) {
                showToast('Блок отчёта не найден в документе', 'error');
                return;
            }

            // Клонируем содержимое и заменяем поля ввода на текст
            var clone = content.cloneNode(true);
            var inputs = clone.querySelectorAll('.report-doc__input');
            for (var i = 0; i < inputs.length; i++) {
                var inp = inputs[i];
                var span = document.createElement('span');
                span.textContent = inp.value || '—';
                span.style.fontWeight = '600';
                span.style.color = '#000';
                inp.parentNode.replaceChild(span, inp);
            }

            var htmlContent = clone.innerHTML;
            if (!htmlContent || htmlContent.length < 30) {
                showToast('Содержимое отчёта пустое', 'error');
                return;
            }

            var docHtml =
                '<html xmlns:o="urn:schemas-microsoft-com:office:office" ' +
                'xmlns:w="urn:schemas-microsoft-com:office:word" ' +
                'xmlns="http://www.w3.org/TR/REC-html40">' +
                '<head>' +
                '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">' +
                '<meta charset="utf-8">' +
                '<title>Технический отчёт по результатам инженерных расчётов</title>' +
                '<!--[if gte mso 9]>' +
                '<xml>' +
                '<w:WordDocument>' +
                '<w:View>Print</w:View>' +
                '<w:Zoom>100</w:Zoom>' +
                '<w:DoNotOptimizeForBrowser/>' +
                '</w:WordDocument>' +
                '</xml>' +
                '<![endif]-->' +
                '<style>' +
                '@page { size: A4 portrait; margin: 2cm 1.5cm; }' +
                'body { font-family: "Times New Roman", "Liberation Serif", serif; ' +
                'font-size: 12pt; color: #000; margin: 0; line-height: 1.45; }' +
                'table { border-collapse: collapse; width: 100%; margin: 8pt 0 14pt; }' +
                'td, th { border: 1px solid #000; padding: 5px; font-size: 10.5pt; ' +
                'vertical-align: top; text-align: left; }' +
                'th { background: #e8e8e8; font-weight: bold; text-transform: uppercase; font-size: 10pt; }' +
                'td.num { text-align: right; white-space: nowrap; }' +
                '.report-doc__org { font-weight: bold; text-transform: uppercase; font-size: 12pt; }' +
                '.report-doc__header { text-align: center; border-bottom: 2pt solid #000; ' +
                'padding-bottom: 8pt; margin-bottom: 12pt; font-size: 11pt; line-height: 1.55; }' +
                '.report-doc__header > div { margin: 2pt 0; }' +
                '.report-doc__title { text-align: center; font-size: 13pt; font-weight: bold; ' +
                'text-transform: uppercase; letter-spacing: .04em; margin: 14pt 0 6pt; }' +
                '.report-doc__date { text-align: right; font-size: 10pt; color: #333; ' +
                'font-style: italic; margin-bottom: 12pt; }' +
                '.report-doc__section { margin: 14pt 0; }' +
                '.report-doc__section-title { font-size: 11.5pt; font-weight: bold; ' +
                'text-transform: uppercase; letter-spacing: .04em; margin: 0 0 8pt; ' +
                'padding-bottom: 4pt; border-bottom: 1.5pt solid #000; }' +
                '.report-doc__info-table { width: 100%; border-collapse: collapse; margin: 6pt 0; }' +
                '.report-doc__info-table td { border: 1px solid #000; padding: 6pt 8pt; vertical-align: middle; }' +
                '.report-doc__info-label { width: 32%; background: #f0f0f0; font-weight: bold; ' +
                'text-transform: uppercase; font-size: 9.5pt; }' +
                '.report-doc__conclusion { border: 1pt solid #000; padding: 8pt 12pt; margin: 0; }' +
                '.report-doc__conclusion p { font-size: 11pt; line-height: 1.6; ' +
                'text-align: justify; margin: 0; }' +
                '.report-doc__signature { margin-top: 30pt; font-size: 11pt; line-height: 2; }' +
                '.report-doc__signature-line { display: inline-block; ' +
                'border-bottom: 1pt solid #000; min-width: 120pt; height: 1em; ' +
                'margin: 0 6pt; vertical-align: bottom; }' +
                '.report-doc__mp { margin-top: 6pt; font-size: 10pt; color: #333; }' +
                'tr.section-row td { background: #f0f0f0; font-weight: bold; ' +
                'text-transform: uppercase; font-size: 10pt; letter-spacing: .03em; }' +
                '</style>' +
                '</head>' +
                '<body>' + htmlContent + '</body>' +
                '</html>';

            var htmlWithBom = '\uFEFF' + docHtml;
            var fileName = 'report.doc';

            var blob = null;
            try {
                blob = new Blob([htmlWithBom], { type: 'application/msword;charset=utf-8' });
            } catch (eBlob) {
                console.warn('[downloadWord] Blob creation failed:', eBlob);
                blob = null;
            }

            if (window.navigator && typeof window.navigator.msSaveOrOpenBlob === 'function' && blob) {
                window.navigator.msSaveOrOpenBlob(blob, fileName);
                showToast('Файл ' + fileName + ' сформирован', 'success');
                return;
            }

            if (blob && window.URL && typeof window.URL.createObjectURL === 'function') {
                var url = URL.createObjectURL(blob);
                var link = document.createElement('a');
                link.href = url;
                link.download = fileName;
                link.rel = 'noopener';
                link.style.display = 'none';
                document.body.appendChild(link);

                if (typeof link.click === 'function') {
                    link.click();
                } else {
                    var evt = document.createEvent('MouseEvents');
                    evt.initMouseEvent('click', true, true, window, 0, 0, 0, 0, 0,
                                       false, false, false, false, 0, null);
                    link.dispatchEvent(evt);
                }

                setTimeout(function () {
                    if (link.parentNode) link.parentNode.removeChild(link);
                    try { URL.revokeObjectURL(url); } catch (e) {}
                }, 1500);

                showToast('Файл ' + fileName + ' сформирован', 'success');
                return;
            }

            try {
                var dataUri = 'data:application/msword;charset=utf-8,' +
                              encodeURIComponent(htmlWithBom);
                var a = document.createElement('a');
                a.href = dataUri;
                a.download = fileName;
                a.style.display = 'none';
                document.body.appendChild(a);
                a.click();
                setTimeout(function () {
                    if (a.parentNode) a.parentNode.removeChild(a);
                }, 1500);
                showToast('Файл ' + fileName + ' сформирован (fallback)', 'success');
                return;
            } catch (eUri) {
                console.error('[downloadWord fallback URI]', eUri);
            }

            showToast('Не удалось создать файл в этом браузере', 'error');
        } catch (err) {
            console.error('[downloadWord]', err);
            showToast('Ошибка при создании файла: ' + (err && err.message ? err.message : err), 'error');
        }
    }

    /* =================================================================
       СОХРАНЕНИЕ / ЗАГРУЗКА ПРОЕКТА
       ================================================================= */
    function saveProject() {
        var project = {
            version: 2,
            savedAt: new Date().toISOString(),
            reportMeta: Object.assign({}, state.reportMeta),
            modules: {
                1: { values: Object.assign({}, state.modules[1].values) },
                2: { values: Object.assign({}, state.modules[2].values) },
                3: { values: Object.assign({}, state.modules[3].values) }
            }
        };
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(project));
            showToast('Проект сохранён в браузере', 'success');
        } catch (e) {
            showToast('Не удалось сохранить: ' + e.message, 'error');
        }
    }

    function loadProject() {
        var raw = null;
        try { raw = localStorage.getItem(STORAGE_KEY); } catch (e) {}
        if (!raw) return false;

        var project;
        try { project = JSON.parse(raw); } catch (e) { return false; }
        if (!project || !project.modules) return false;

        // Восстанавливаем общие сведения
        var metaSource = project.reportMeta || project.meta;
        if (metaSource) {
            Object.keys(metaSource).forEach(function (k) {
                if (k in state.reportMeta) {
                    state.reportMeta[k] = metaSource[k];
                }
            });
        }

        // Восстанавливаем значения модулей
        Object.keys(project.modules).forEach(function (midStr) {
            var mid = Number(midStr);
            if (!state.modules[mid]) return;
            var savedValues = project.modules[midStr].values || {};
            Object.keys(savedValues).forEach(function (key) {
                if (key in state.modules[mid].values) {
                    state.modules[mid].values[key] = savedValues[key];
                }
            });
        });
        return true;
    }

    /* =================================================================
       ИНИЦИАЛИЗАЦИЯ
       ================================================================= */
    function init() {
        initTheme();

        var themeToggle = $('#themeToggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', function () {
                applyTheme(state.theme === 'dark' ? 'light' : 'dark');
            });
        }

        var restored = loadProject();

        $$('.tab').forEach(function (tab) {
            tab.addEventListener('click', function () { switchTab(tab.dataset.tab); });
        });

        $$('.field__input').forEach(function (input) {
            var moduleId = Number(input.dataset.module);
            var key = input.dataset.key;

            var saved = state.modules[moduleId].values[key];
            if (saved !== undefined && saved !== null) {
                input.value = saved;
            }

            var handler = function () {
                state.modules[moduleId].values[key] = input.value;
                calculateModule(moduleId);
                renderReportDocument();
            };

            input.addEventListener('input', handler);
            input.addEventListener('change', handler);

            input.addEventListener('keydown', function (e) {
                if (e.key === '-' || e.key === 'e' || e.key === 'E' || e.key === '+') {
                    e.preventDefault();
                }
            });

            input.addEventListener('paste', function (e) {
                var text = (e.clipboardData || window.clipboardData).getData('text');
                if (text && text.indexOf('-') !== -1) {
                    e.preventDefault();
                }
            });
        });

        // ---- Делегирование ввода для полей блока «1. Общие сведения» ----
        // Слушатель висит на контейнере, который не пересоздаётся при
        // renderReportDocument() — работает даже после многократных перерисовок
        var reportContainer = $('#reportDocument');
        if (reportContainer) {
            reportContainer.addEventListener('input', handleReportMetaInput);
        }

        $$('[data-action]').forEach(function (btn) {
            var action = btn.dataset.action;
            var moduleId = Number(btn.dataset.module);

            btn.addEventListener('click', function () {
                if (action === 'calc') {
                    calculateModule(moduleId);
                    renderReportDocument();
                    showToast('Модуль ' + moduleId + ' пересчитан', 'info');
                } else if (action === 'reset') {
                    resetModule(moduleId);
                } else if (action === 'print') {
                    calculateModule(moduleId);
                    window.print();
                }
            });
        });

        var transferM1 = $('#transferFromM1');
        if (transferM1) {
            transferM1.addEventListener('click', function () {
                transferCommonParam(1, [2, 3]);
            });
        }

        var transferM2 = $('#transferFromM2');
        if (transferM2) {
            transferM2.addEventListener('click', function () {
                transferCommonParam(2, [3]);
            });
        }

        var genReport = $('#generateReport');
        if (genReport) genReport.addEventListener('click', generateReport);

        var downloadBtn = $('#downloadWord');
        if (downloadBtn) downloadBtn.addEventListener('click', downloadWord);

        var saveBtn = $('#saveProject');
        if (saveBtn) saveBtn.addEventListener('click', saveProject);

        var printReport = $('#printReport');
        if (printReport) {
            printReport.addEventListener('click', function () {
                renderReportDocument();
                switchTab('4');
                setTimeout(function () { window.print(); }, 150);
            });
        }

        calculateModule(1);
        calculateModule(2);
        calculateModule(3);
        renderReportDocument();

        if (restored) {
            showToast('Загружен последний сохранённый проект', 'info');
        }

        window.addEventListener('storage', function (e) {
            if (e.key === THEME_KEY && e.newValue) {
                applyTheme(e.newValue);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
</script>
</body>
</html>