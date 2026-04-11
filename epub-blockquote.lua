-- epub-blockquote.lua
-- Applies inline styles directly to blockquotes in EPUB output.
-- External CSS border-left/background-color is ignored by many e-readers;
-- inline styles have near-universal support.

if FORMAT:match("epub") then
  function BlockQuote(el)
    local style = table.concat({
      "font-style:italic",
      "margin:1.5em 0.5em",
      "padding:0.75em 1em 0.75em 1.2em",
      "border-left:3pt solid #9B7E5A",
      "background-color:#FAF6F0",
      "line-height:1.5",
    }, ";")

    local div = pandoc.Div(el.content)
    div.attr = pandoc.Attr("", {}, {style = style})
    return div
  end
end
