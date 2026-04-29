---
title: Заготовка схемы для draw.io
order: 1
---

## Описание

Ниже размещён минимальный XML-фрагмент, который можно использовать как основу для схемы в draw.io.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="order-flow" name="Order Flow">
    <mxGraphModel dx="1024" dy="768" grid="1" gridSize="10" guides="1" tooltips="1" connect="1">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" value="Витрина" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="120" width="140" height="50" as="geometry" />
        </mxCell>
        <mxCell id="3" value="Сервис расчёта" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="120" width="180" height="50" as="geometry" />
        </mxCell>
        <mxCell id="4" value="Итоговая сумма" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Примечание

В демонстрационных целях схема хранится прямо в Markdown-документе, чтобы весь контент репозитория оставался в формате `.md`.